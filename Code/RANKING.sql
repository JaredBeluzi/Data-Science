/* 
Bsp: letzte Adresse einer Person finden
Adresse
Adresse_ID   Person_ID   Adresse_gültig_von   Adresse_gültig_bis   Adresse_Straße   Adresse_Hausnummer    RANKING
1            1           01.01.2019           01.06.2019           Haupstraße       5                     4
2            1           03.06.2019           01.01.2023           Haupstraße       4                     3
3            1           01.01.2020           01.01.2023           Haupstraße       10                    2
4            1           01.01.2020           01.01.2023           Haupstraße       50                    1		<-- Die Adresse hier würde man dann ausgeben für die Person
*/

SELECT
	SUB.Person_ID
,	SUB.Adresse_Straße
,	SUB.Adresse_Hausnummer
INTO	dbo.Ergebnis
FROM
(
SELECT 
	Person.Person_ID
	Adresse.Adresse_Straße
,	Adresse.Adresse_Hausnummer
,	RANK() OVER ( PARTITION BY Person.Person_ID ORDER BY 	
        	Adresse.Adresse_gültig_bis DESC
	,	Adresse.Adresse_gültig_von DESC
	,	Adresse.Adresse_ID DESC) AS RANKING -- als letzten Rankingfaktor ID nehmen, um Eindeutigkeit bei Datenmüll zu erzwingen
FROM dbo.Person AS Person
INNER JOIN dbo.Adresse AS Adresse
    ON Person.Person_ID = Adresse.Person_ID
) AS SUB
WHERE SUB.RANKING = 1
