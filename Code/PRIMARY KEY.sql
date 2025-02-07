-- Spalte muss UNIQUE values beinhalten und NULL ist nicht erlaubt. 
-- Trifft eines der beiden nicht zu, läuft der Befehlt auf einen Fehler.

ALTER TABLE dbo.Tabelle
ADD PRIMARY KEY (Spalte)

-- NULL-Werte kann man so im Voraus verbieten:
ALTER TABLE dbo.Tabelle
ALTER COLUMN Spalte Datentyp NOT NULL -- Datentyp sollte derselbe sein wie zuvor

-- UNIQUEness kann man so im Voraus erzwingen:
ALTER TABLE dbo.Tabelle
ALTER COLUMN Spalte Datentyp NOT NULL UNIQUE -- Datentyp sollte derselbe sein wie zuvor
