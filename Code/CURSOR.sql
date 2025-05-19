DECLARE @i VARCHAR(100); -- Laufvariable, die durch Spalte läuft
DECLARE @SQL NVARCHAR(MAX); -- dynamischer SQL

-- Cursor definieren und öffnen
DECLARE Körser CURSOR FOR 
SELECT 
	[Text]
FROM dbo.ES_51505

OPEN Körser;

FETCH NEXT FROM Körser INTO @i; -- erste Zeile in Cursor fetchen

-- Durch Cursor loopen
WHILE @@FETCH_STATUS = 0
BEGIN
    SET @SQL = N'
    SELECT ''' + @i + ''' AS a
	';

    EXEC sp_executesql @SQL;
    
    FETCH NEXT FROM Körser INTO @i; -- nächste Zeile fetchen
END;

-- Cursor schlie0en
CLOSE Körser;
DEALLOCATE Körser;
