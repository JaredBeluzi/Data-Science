/*
Problem: Man hat 2 Tabellen, die man nicht 1-1 matchen kann, aber 2-2 oder 3-3 ... 
Dann will man diese Matches trotzdem benutzen. Bsp:

Tabelle "Groß"        Tabelle "klein"     -->      Tabelle "Zuordnung"  
Groß_ID  Groß_Name    klein_ID  klein_Name         Groß_ID  klein_ID
A        Alex         a         Alex               A        a
B        Alex         b         Alex               B        b
C        Max          c         Max                C        c
D        Max          d         Max                D        d
E	 Max          e		Max	           E        e

Man weiß hier, dass A und B zu a und b gehören, aber nicht genau wie. Das ist aber auch egal. Man will sie random zuordnen und dabei alle IDs verwenden. Deshalb ist das Ziel hier Tabelle 3.
*/
SELECT
	Groß.Groß_ID
,	klein.klein_ID
,	RANK() OVER ( PARTITION BY Groß.Groß_ID ORDER BY klein.klein_ID ASC) AS klein_RANKING
,	RANK() OVER ( PARTITION BY klein.klein_ID ORDER BY Groß.Groß_ID ASC) AS Groß_RANKING
INTO	  dbo.Zuordnung
FROM		dbo.Groß AS Groß
INNER JOIN	dbo.klein AS klein
    ON Groß.Groß_Name = klein.klein_Name

DELETE FROM dbo.Zuordnung
WHERE klein_RANKING <> Groß_RANKING

/*
Die Ausgabe vor dem DELETE wäre hier:              und dementsprechend nach dem DELETE:

Tabelle "Zuordnung"                                Tabelle "Zuordnung"
Groß_ID  klein_ID  Groß_RANKING  klein_RANKING     Groß_ID  klein_ID  Groß_RANKING  klein_RANKING
A        a         1             1                 A        a         1             1
A        b         1             2                 B        b         2             2
B        a         2             1                 C        c         1             1
B        b         2             2                 D        d         2             2
C        c         1             1                 E        e         3             3
C        d         1             2
C        e         1             3
D        c         2             1
D        d         2             2
D        e         2             3
E        c         3             1
E        d         3             2
E        e         3             3

*/
