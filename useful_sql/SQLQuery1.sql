SELECT OBJECT_NAME(OBJECT_ID) AS Object_, last_user_update lup,*
FROM sys.dm_db_index_usage_stats
WHERE database_id = DB_ID( 'pharmsourcecom')
ORDER BY lup DESC

SELECT *
FROM tblCompanies
ORDER BY CompanyID DESC

SELECT *
FROM edtCompanies
ORDER BY CompanyID DESC

SELECT *
FROM 