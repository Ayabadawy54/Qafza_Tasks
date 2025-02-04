USE [master]
GO
CREATE LOGIN [ETL] WITH PASSWORD=N'ETLProject', DEFAULT_DATABASE=[AdventureWorks2022], CHECK_EXPIRATION=OFF, CHECK_POLICY=OFF
GO
USE [AdventureWorks2022]
GO
CREATE USER [ETL] FOR LOGIN [ETL]
GO
USE [AdventureWorks2022]
GO
ALTER ROLE [db_datareader] ADD MEMBER [ETL]
GO
use [master]
GO
GRANT CONNECT SQL TO [ETL]
GO

use AdventureWorks2022
select * from HumanResources.Department;