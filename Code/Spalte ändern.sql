---------------------------
---- Spalte umbenennen ----
---------------------------

EXEC sp_rename 'dbo.Tabelle.alter_Spaltenname' , 'neuer_Spaltenname' , 'COLUMN';


-------------------------
---- Datentyp ändern ----
-------------------------

ALTER TABLE dbo.Tabelle
ALTER COLUMN Spaltenname neuer_Datentyp


------------------------
---- Spalte löschen ----
------------------------

ALTER TABLE dbo.Tabelle
DROP COLUMN Spaltenname


----------------------
---- Spalte adden ----
----------------------

ALTER TABLE dbo.Tabelle
ADD Spaltenname Datentyp
