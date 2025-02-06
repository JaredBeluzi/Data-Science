----------------------------
---- INSERT INTO SELECT ----
----------------------------

-- Code fügt Zeilen aus Select in Tabelle dbo.Personen hinzu

INSERT INTO dbo.Personen (
    Vorname
,   Nachname
) -- Man sollte hier wie oben nochmal die Spalten aufliste. Sonst kann es zu Vertauschungen bei der Spaltenreihenfolge kommen, wenn in diese geschrieben wird.
SELECT 
    n.Vorname
,   n.Nachname
FROM dbo.Person AS p
INNER JOIN  dbo.Name AS n
  ON p.ID = n.ID
