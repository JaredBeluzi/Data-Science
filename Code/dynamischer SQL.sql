
-- ein dynamischer SQL ermöglicht es Variablen innerhalb eines SQL Codes zu verwenden (z.B. für Loops)

-- Die Variable @max_date beinhaltet das Maximum aus der Spalte Datum in ES_51860 + 30 Tage
DECLARE	@Max_Datum AS DateTime
SELECT @Max_Datum = DATEADD(day, 30, MAX(Datum)) FROM dbo.ES_51860

DECLARE @sql VarChar(Max) -- Textvariable erstellen
SET @sql = -- Code in Textvariable schreiben
'
SELECT *
INTO dbo.ES_1010
FROM dbo.ST_vz
WHERE vz_Datum <= ' + @Max_Datum + '
'

EXEC(@sql)-- Code in Textvariable ausführen
