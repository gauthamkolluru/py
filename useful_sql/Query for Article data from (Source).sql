select 
ta.ArticleID, 
ta.SectionID, 
SectionName,
ta.DisplayTitle,
tas.ArticleCategoryID,
SubCategory,
tca.CompanyID,
tc.CompanyName,
HTMLFileName,
--tca.Comp_ArtID, 
ta.DatePosted, 
ta.NotificationDate 
from tblArticles ta
JOIN tblArticles_SubCategories ta_s 
on ta.ArticleID = ta_s.ArticleID 
JOIN tblArticleSubCategories tas 
ON ta_s.SubCategoryID = tas.SubCategoryID 
JOIN tblCompany_Article tca 
ON ta.ArticleID = tca.ArticleID
JOIN tblCompanies tc 
ON tc.CompanyId=tca.CompanyId
JOIN tblsections ts 
ON ts.SectionID=ta.SectionID
GROUP BY
ta.ArticleID, 
ta.SectionID, 
SectionName,
ta.DisplayTitle,
tas.ArticleCategoryID,
tca.CompanyID,
tc.CompanyName,
HTMLFileName,
SubCategory,
--tca.Comp_ArtID, 
ta.DatePosted, 
ta.NotificationDate