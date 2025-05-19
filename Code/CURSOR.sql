DECLARE @i VARCHAR(100); -- Laufvariable, die durch Spalte läuft
DECLARE @SQL NVARCHAR(MAX); -- dynamischer SQL

DECLARE Körser CURSOR FOR -- Cursor definieren auf eine Spalte
SELECT 
	[Text]
FROM dbo.ES_51505

OPEN Körser;

FETCH NEXT FROM Körser INTO @i; -- Fetch the first row

-- Durch Cursor loopen
WHILE @@FETCH_STATUS = 0
BEGIN
    SET @SQL = N'
    SELECT ''' + @i + ''' AS a
	';
    
    -- Execute the dynamic SQL
    EXEC sp_executesql @SQL;
    
    -- Fetch the next row
    FETCH NEXT FROM Körser INTO @i;
END;

-- Clean up the cursor
CLOSE Körser;
DEALLOCATE Körser;
