/*
                      Primary Key         Clustered Index      NonClustered Index
Speed                 am schnellsten      schneller            schnell
Index ist Clustered   ja                  ja                   nein
Werte müssen UNIQUE   ja                  nein                 nein
ist NULL erlaubt      nein                ja                   ja

With a clustered index the rows are stored physically on the disk in the same order as the index.
Therefore, there can be only one clustered index.
With a non clustered index there is a second list that has pointers to the physical rows. 
You can have many non clustered indices, although each new index will increase the time it takes to write new records. 
*/

---- 1. Indices erstellen ----

ALTER TABLE dbo.Tabelle
ADD PRIMARY KEY (Spalte)

CREATE CLUSTERED INDEX IX_Tabelle_Spalte ON dbo.Tabelle (Spalte)

CREATE NONCLUSTERED INDEX IX_Tabelle_Spalte ON dbo.Tabelle (Spalte)


---- 2. Vorbereitung

-- NULL-Werte kann man so im Voraus verbieten:
ALTER TABLE dbo.Tabelle
ALTER COLUMN Spalte Datentyp NOT NULL -- Datentyp sollte derselbe sein wie zuvor

-- UNIQUEness kann man so im Voraus erzwingen:
ALTER TABLE dbo.Tabelle
ALTER COLUMN Spalte Datentyp NOT NULL UNIQUE -- Datentyp sollte derselbe sein wie zuvor
