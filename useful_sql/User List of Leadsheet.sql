SELECT 
 b.company [Company Name],
 a.[SubscriberName]
      ,[Email]
      ,[ActivationDate]
      ,[ExpirationDate]
      ,[LeadsheetPurchased]
      ,'PharmSource LeadSheet' 
  FROM [pharmsrc_leadsheet].[dbo].[tblSubscriber_CLS] c
    left join[pharmsrc_leadsheet].[dbo].[tblSubscribers] a on a.SubscriberID=c.SubscriberID
  left join [pharmsrc_leadsheet].[dbo].[tblSubscriberCompanies] b on a.CompanyID=b.CompanyID
 where b.[company] is not null  
order by b.company, a.[SubscriberName]