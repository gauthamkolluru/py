select 
ta.ArticleID, 
ta.SectionID, 
ta.DisplayTitle,
tas.ArticleCategoryID,
tca.CompanyID,
--tca.Comp_ArtID, 
ta.DatePosted, 
ta.NotificationDate 
from tblArticles ta
join tblArticles_SubCategories ta_s 
on ta.ArticleID = ta_s.ArticleID 
JOIN tblArticleSubCategories tas 
ON ta_s.SubCategoryID = tas.SubCategoryID 
JOIN tblCompany_Article tca 
ON ta.ArticleID = tca.ArticleID
GROUP BY
ta.ArticleID, 
ta.SectionID, 
ta.DisplayTitle,
tas.ArticleCategoryID,
tca.CompanyID,
--tca.Comp_ArtID, 
ta.DatePosted, 
ta.NotificationDate