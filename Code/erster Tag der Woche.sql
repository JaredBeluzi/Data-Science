SELECT
  Datum
, DATEADD(WEEK, DATEDIFF(DAY, '01.01.1900', Datum)/7, '01.01.1900') AS erster_Tag_der_Woche
FROM dbo.Tabelle
