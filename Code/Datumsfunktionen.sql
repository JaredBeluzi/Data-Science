DATEADD(month, -1, '2014/04/28') -- = '2014-03-28 00:00:00.000'
DATEDIFF(day, '2014/01/01', '2014/04/28') -- = 117

YEAR('2014/03/31 10:05') = 2014
MONTH('2014/03/31 10:05') = 3
DAY('2014/03/31 10:05') = 31
DATEPART(second, '2014/04/28 09:49:12') -- = 12 (integer)
DATENAME(month, '2014/04/28 09:49:12') -- = April

GetDate() -- heutiges Datum 2014-05-01 15:29:59.917

------------------------------
---- erster Tag der Woche ----
------------------------------
  
SELECT
  Datum
, DATEADD(WEEK, DATEDIFF(DAY, '01.01.1900', Datum)/7, '01.01.1900') AS erster_Tag_der_Woche
FROM dbo.Tabelle
