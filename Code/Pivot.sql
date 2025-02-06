--------------------------
---- statischer Pivot ----
--------------------------

/*
Beispieltabelle					Ergebnis
Person        ICD_Gruppe   Diagnose_Jahr        ICD_Gruppe   2030    2031
-----------------------------------------       -------------------------
John          F            2030                 F            2       0
Jack          F            2030                 G            1       2
Josh          G            2030                 H            0       2
Jacob  pear   G            2031
Jacobson      G            2031
Johnson       H            2031
JoJo          H            2031
*/

SELECT
	ICD_Gruppe
,	[2030]
,	[2031]
INTO	dbo.Ergebnis
FROM   
(
	SELECT -- Reihenfolge der Spalten hier ist egal
		Diagnose_Jahr	-- Spaltennamen für Pivottabelle
	,	ICD_Gruppe	-- Zeilen für Pivottabelle
	,	Person          -- Werte, die aggregiert werden
	FROM	dbo.ICD
) t 
PIVOT(
    COUNT(Person) -- man kann hier auch andere Aggregationsfunktionen benutzen
    FOR Diagnose_Jahr IN (
			[2030] -- Man muss jeden Wert in [] schreiben
		,	[2031]
		)
) AS Pivottabelle

----------------------------------------------------------------
---- dynamischer Pivot (Spaltenliste automatisch bestimmen) ----
----------------------------------------------------------------
/*
Beispieltabelle						Ergebnis
Person        ICD_Gruppe   Diagnose_Jahr    		ICD_Gruppe   2030    2031
-----------------------------------------               -------------------------
John          F            2030     	                F            2       0
Jack          F            2030                         G            1       2
Josh          G            2030                         H            0       2
Jacob  pear   G            2031
Jacobson      G            2031
Johnson       H            2031
JoJo          H            2031
*/

-- Variablen initiieren
DECLARE @Spaltenliste AS VarChar(Max)
DECLARE @sql AS VarChar(Max)

-- Alle DISTINCT Were aus diagnosis_year in Variable für Spaltenliste schreiben
SET @Spaltenliste = (
SELECT TOP 1 
	Diagnose_Jahr = STUFF(( 
				SELECT DISTINCT   -- nur DISTINCT Werte in Liste schreiben
				', '
				,	QUOTENAME(Diagnose_Jahr) -- dadurch Formatierung, die Werte in [] packt
				FROM dbo.ICD
				FOR XML PATH('')) -- schreibt alle Werte nacheinander in einen Text
				,1,1,'')          -- entfernt das erste Komma in dem Text
FROM dbo.ICD)
--  Ergebnis wäre hier: @col_list = '[2030], [2031]'

-- dynamischen SQL schreiben
SET @sql = '
SELECT * 
INTO	dbo.Ergebnis
FROM  
(
	SELECT 
		Diagnose_Jahr	-- beinhaltet Spaltennamen für Pivot
	,	ICD_Gruppe	-- beinhaltet Zeilen
	,	Person		-- Werte, die aggregiert werden sollen im Pivot
	FROM	dbo.ICD
) t 
PIVOT(
    COUNT(Person) 
    FOR Diagnose_Jahr IN (' + @Spaltenliste + ')
	) AS Pivottabelle
' 
	
EXEC(@sql) -- dynamischen SQL ausführen
