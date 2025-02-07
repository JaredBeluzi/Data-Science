WITH geordnete_Liste AS (
  SELECT DISTINCT TOP 100000000000000
		ID
	,	Textspalte
	FROM dbo.Tabelle
	ORDER BY
		ID
	,	Kriterium
	,	Textspalte
)
SELECT
	ID
,	STRING_AGG(Textspalte, ', ') AS Textliste
FROM	geordnete_Liste
GROUP BY
	ID
