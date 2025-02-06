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

----------------------------
---- INSERT INTO VALUES ----
----------------------------
    
-- Code fügt manuell Zeilen in Tabelle hinzu

INSERT INTO dbo.Namen (
    Vorname
,   Nachname
) -- Hier oben alle Spalten explizit nennen. Sonst kann Spaltenreihenfolge durcheinander kommen beim Befüllen der Spalten.
VALUES
  ('Peter', 'Arndt')
, ('Luisa', 'Scharafinski')
, ('Robert', 'Ullrich')
