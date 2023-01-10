/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [TIPO_TRANSPORTE]
      ,[DIA]
      ,[PARCIAL]
      ,[CANTIDAD]
  FROM [MODELOS].[dbo].[dataset_viajes_sube]

  SELECT
    CASE WHEN [PARCIAL]IS NULL THEN 10
    ELSE PARCIAL
    END AS Total
  FROM [MODELOS].[dbo].[dataset_viajes_sube];

   SELECT   
    CASE WHEN [CANTIDAD]IS NULL THEN 10
    ELSE PARCIAL
    END AS Total
   FROM [MODELOS].[dbo].[dataset_viajes_sube];

   SELECT *
      ,[DIA]
      ,[PARCIAL]
      ,[CANTIDAD]
  FROM [MODELOS].[dbo].[dataset_viajes_sube]

  UPDATE [dbo].[dataset_viajes_sube]
    SET [PARCIAL] = '1' 

	UPDATE [dbo].[dataset_viajes_sube]
    SET [CANTIDAD] = '100' 

	SELECT * FROM [MODELOS].[dbo].[dataset_viajes_sube]

	select * from [MODELOS].[dbo].[dataset_viajes_sube]
	where TIPO_TRANSPORTE ='colectivo'
	order by DIA
	;
	

	SELECT   
    CASE WHEN [TIPO_TRANSPORTE]IS NULL THEN CANTIDAD
    ELSE PARCIAL
    END AS Total
   FROM [MODELOS].[dbo].[dataset_viajes_sube];
