-----------------------------------------------------------
-- 1. Bestimme alle Beginnzeitpunkte von Zeitabschnitten --
-----------------------------------------------------------

SELECT DISTINCT
	v_ID
,	Zeitraum_von
INTO	dbo.{Anzeigesicht}
FROM	dbo.ES_12345
UNION	-- doppelte müssen herausgeworfen werden
SELECT DISTINCT
	v_ID
,	DateAdd(day, 1, Zeitraum_bis) AS Zeitraum_von
FROM	dbo.ES_51504

-----------------------------------------------------------
--------- 2. Erstelle Tabelle mit Zeitabschnitten ---------
-----------------------------------------------------------

SELECT
	v_ID
,       Zeitraum_von
,	CAST(DATEADD(day, -1, LEAD(Zeitraum_von, 1) OVER (	PARTITION BY 	v_ID
								ORDER BY Zeitraum_von ASC))
	AS Date)  AS Zeitraum_bis
,	Cast(0 AS Int) AS Tage
,	Cast('-' AS VarChar(100)) AS Kategorie
INTO	dbo.{Anzeigesicht}
FROM	dbo.ES_12334

-- Dauer berechnen
UPDATE	a
SET 	a.Tage = DateDiff(day, Zeitraum_von, Zeitraum_bis) + 1
FROM	dbo.{Anzeigesicht} AS a

----------------------------------------------------------
------------ 3. Zeitabschnitte kategorisieren ------------
----------------------------------------------------------

UPDATE	a
SET	a.Kategorie = 'Käse'
FROM	dbo.{Anzeigesicht} AS a
INNER JOIN	dbo.ES_54321 AS b
	ON a.v_ID = b.v_ID
WHERE b.Nahrungsmittel = Käse


-- Dasselbe für jede Kategorie machen



