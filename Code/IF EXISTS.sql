/*
Code prüft ob Tabelle ST_HelicDynamic (mit Spalte HelicDynamic_Status) existiert und führt nur dann SQL aus.
*/

IF EXISTS(
		SELECT o.* 
		FROM 		      sys.objects AS o
		INNER JOIN		sys.columns AS c -- JOIN entfernen, wenn man nur prüfen will ob Tabelle an sich existiert
			ON	o.object_ID = c.object_ID
 		WHERE o.Name = 'ST_HelicDynamic'
		AND   c.Name = 'HelicDynamic_Status') -- ebenfalls entfernen, wenn man nur prüfen will ob Tabelle an sich existiert

BEGIN

-- Hier SQL schreiben, der dann ausgeführt werden soll

END
