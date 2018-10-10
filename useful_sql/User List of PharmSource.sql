SELECT 
      
       [UserName]
       ,[FullName]
     ,Name[Contact Person]
     ,Employer [Employer/Company]
      ,[Address] Email
      ,StartDate
      ,EndDate
      ,Active
      ,'Strategic Advantage' [Site Name]
  FROM [pharmsourcecom].[dbo].[tblUsers] a
  left join [pharmsourcecom].[dbo].[tblSubscribers] b on a.SubscriberID=b.SubscriberID
  left join [pharmsourcecom].[dbo].[tblSubscriberPeriods] c on b.SubscriberID=c.SubscriberID
  left join [pharmsourcecom].[dbo].[tblUserEMail] d on a.userID=d.UserID