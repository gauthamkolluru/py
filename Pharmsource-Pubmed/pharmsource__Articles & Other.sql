SELECT * FROM Pubmed_Master_Medlinecitation where id = 2208 --CreatedDate <> ModifiedDate

SELECT * FROM Pubmed_Master_Abstracttext WHERE Medlinecitation_id = 2208

SELECT * FROM Pubmed_Master_Author WHERE Medlinecitation_id = 2208

SELECT * FROM Pubmed_Master_meshheading WHERE Medlinecitation_id = 2208

SELECT TOP 2 * FROM Pubmed_Medlinecitation WHERE PMID = 28872337 --order BY ID DESC --where PMID = 28872337 

SELECT * FROM Pubmed_Abstracttext WHERE Medlinecitation_id = 5853

SELECT * FROM Pubmed_author WHERE Medlinecitation_id = 5853

SELECT TOP 2 * FROM Pubmed_meshheading WHERE Medlinecitation_id = 5853 --ORDER BY id DESC 

--TRUNCATE table Pubmed_Master_Medlinecitation

--TRUNCATE table Pubmed_Master_Abstracttext

--TRUNCATE table Pubmed_Master_Author

--TRUNCATE table Pubmed_Master_meshheading

--TRUNCATE table Pubmed_Medlinecitation

--TRUNCATE table Pubmed_Abstracttext

--TRUNCATE table Pubmed_author

--TRUNCATE table Pubmed_meshheading

--delete from Pubmed_Master_Medlinecitation where ID =1
--delete from Pubmed_Master_Abstracttext --where Medlinecitation_id >2
--delete from Pubmed_Master_Author --where Medlinecitation_id >2
--delete from Pubmed_Master_meshheading --where Medlinecitation_id >2
--delete from Pubmed_Medlinecitation where ID >2
--delete from Pubmed_Abstracttext where Medlinecitation_id >2
--delete from Pubmed_author where Medlinecitation_id >2
--delete from Pubmed_meshheading where Medlinecitation_id >2





SELECT * FROM tblArticles

SELECT * FROM tblArticleCategories

SELECT * FROM tblArticles_SubCategories

SELECT * FROM tblArticleSubCategories