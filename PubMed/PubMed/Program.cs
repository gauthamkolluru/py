using AutoMapper;
using System;
using System.Collections.Generic;
using System.Configuration;
using System.Data;
using System.Data.SqlClient;
using System.IO;
using System.IO.Compression;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;
using System.Xml;
using System.Xml.Serialization;

namespace PubMed
{

    class Program
    {

        static void Main(string[] args)
        {
           // QueryNIH();
            //Environment.Exit(0);

            BuildDataTableFromXml("pubmed18n1304.xml");

           // ReadDownloads("17oct.xml");
        }


        public static void QueryNIH()
        {
            CreateLogFiles Err = new CreateLogFiles();
            Err.ErrorLog("PubMed xml.zp file download started.");

            string fileName = "";
            string ftpURL = "ftp://ftp.ncbi.nlm.nih.gov/pubmed/updatefiles/";

            try
            {
                FtpWebRequest directoryrequest = (FtpWebRequest)WebRequest.Create(ftpURL);
                directoryrequest.Method = WebRequestMethods.Ftp.ListDirectoryDetails;

                //Enter FTP Server credentials.
                directoryrequest.Credentials = new NetworkCredential("", "");
                directoryrequest.UsePassive = true;
                directoryrequest.UseBinary = true;
                directoryrequest.EnableSsl = false;

                //Fetch the Response and read it using StreamReader.
                FtpWebResponse dirresponse = (FtpWebResponse)directoryrequest.GetResponse();
                List<string> entries = new List<string>();
                using (StreamReader reader = new StreamReader(dirresponse.GetResponseStream()))
                {
                    //Read the Response as String and split using New Line character.
                    entries = reader.ReadToEnd().Split(new string[] { Environment.NewLine }, StringSplitOptions.RemoveEmptyEntries).ToList();
                }
                dirresponse.Close();

                for (int i = entries.Count - 3; i < entries.Count - 1; i++)
                {
                    fileName = entries[i].Split(new string[] { " ", }, StringSplitOptions.RemoveEmptyEntries).Last();
                    if (fileName.Split(new string[] { ".", }, StringSplitOptions.RemoveEmptyEntries).Last().ToLower() == "gz")
                        break;
                }



                FtpWebRequest request = (FtpWebRequest)WebRequest.Create(ftpURL + fileName);
                request.Credentials = new NetworkCredential("", "");
                request.UseBinary = true; // Use binary to ensure correct dlv!
                request.Method = WebRequestMethods.Ftp.DownloadFile;
                ServicePointManager.SecurityProtocol = SecurityProtocolType.Ssl3;

                FtpWebResponse response = (FtpWebResponse)request.GetResponse();
                Stream responseStream = response.GetResponseStream();
                FileStream writer = new FileStream(fileName, FileMode.Create);


                long length = response.ContentLength;
                int bufferSize = 2048;
                int readCount;
                byte[] buffer = new byte[2048];

                readCount = responseStream.Read(buffer, 0, bufferSize);
                while (readCount > 0)
                {
                    writer.Write(buffer, 0, readCount);
                    readCount = responseStream.Read(buffer, 0, bufferSize);
                }

                responseStream.Close();
                response.Close();
                writer.Close();

                Err.ErrorLog("PubMed "+ fileName + " file download completed.");

                ReadDownloads(fileName);

            }
            catch (Exception ex)
            {
                Err.ErrorLog(ex.ToString());
            }
        }

        public static void ReadDownloads(string fileName)
        {
            try
            {
                CreateLogFiles Err = new CreateLogFiles();
                Err.ErrorLog("PubMed xml.zp file Extraction started.");

                FileInfo fi = new FileInfo(fileName);
                string curFile = fi.FullName;
                curFile = curFile.Replace(fileName, "Extracts\\" + fileName);
                string origName = curFile.Remove(curFile.Length - fi.Extension.Length);
                FileStream outFile = File.Create(origName);
                FileStream stream = new FileStream(fileName, FileMode.Open);
                using (GZipStream Dc = new GZipStream(stream, CompressionMode.Decompress))
                {
                    Dc.CopyTo(outFile);
                }
                outFile.Close();
                stream.Close();

                Err.ErrorLog("PubMed xml.zp file Extraction completed.");

                BuildDataTableFromXml(outFile.Name);

            }

            catch (Exception ex)
            {
                CreateLogFiles Err = new CreateLogFiles();
                Err.ErrorLog(ex.ToString());
            }
        }

        public static void UpdateChildNodes(XmlNode node)
        {
            foreach (XmlNode item in node.ChildNodes)
            {
                if (item.Name == "ArticleTitle" || item.Name == "AbstractText" || item.Name == "Keyword"
                    || item.Name == "Affiliation" || item.Name == "ELocationID" || item.Name == "CopyrightInformation")
                    item.InnerText = item.InnerText;
                else
                {
                    if (item.ChildNodes.Count == 0)
                        item.InnerText = item.InnerText;
                    else
                        UpdateChildNodes(item);
                }
            }
        }
        public static void BuildDataTableFromXml(string XMLString)
        {
            try
            {

                CreateLogFiles Err = new CreateLogFiles();
                Err.ErrorLog("PubMed xml data inserting into tables started.");

                XmlDocument doc = new XmlDocument();
                doc.Load(XMLString);

                XmlDocumentType XDType = doc.DocumentType;

                if (XDType != null)
                    doc.RemoveChild(XDType);

                foreach (XmlNode node in doc)
                {
                    if (node.NodeType == XmlNodeType.XmlDeclaration)
                    {
                        doc.RemoveChild(node);
                    }
                    foreach (XmlNode mnode in doc)
                    {
                        foreach (XmlNode child in mnode.ChildNodes)
                        {
                            child.InnerXml = child.InnerXml.Replace("<sup />", "").Replace("<sub>", "").Replace("</sub>", "").Replace("<sup>", "").Replace("</sup>", "").Replace("<i>", "").Replace("</i>", "").Replace("<p>", "").Replace("</p>", "").Replace("<b>", "").Replace("</b>", "").Replace("<strong>", "").Replace("</strong>", "").Replace("©", "");
                            UpdateChildNodes(child);
                        }
                    }
                }
                doc.Save(XMLString);
                XmlSerializer serializer = new XmlSerializer(typeof(PubmedArticleSet));
                FileStream fs = new FileStream(XMLString, FileMode.Open);
                XmlReader reader = XmlReader.Create(fs);
                PubmedArticleSet pubData;
                pubData = (PubmedArticleSet)serializer.Deserialize(reader);

                dynamic medlinecitation;
                try { medlinecitation = pubData.PubmedArticle.Select(x => x.MedlineCitation).ToList(); }
                catch { medlinecitation = null; }

                TestDBEntities1 DBContext = new TestDBEntities1();

                if (medlinecitation != null)
                {
                    //foreach (var data in medlinecitation)
                    //{
                    //    DBContext.tb_pmid.Add(new tb_pmid()
                    //    {
                    //        pmid = data.PMID.Text,
                    //        version = data.PMID.Version
                    //    });
                    //    DBContext.SaveChanges();
                    //}


                    foreach (var data in medlinecitation)
                    {
                        int medlineLastid;
                        var strarticledate = string.Empty;
                        var strtitle = string.Empty;
                        var strCountry = string.Empty;
                        var strmonth = string.Empty;
                        var stryear = string.Empty;
                        var strday = string.Empty;
                        var strpubdate = string.Empty;  //list
                        var strLinktoPubmed = string.Empty;
                        try
                        {
                            stryear = data.Article.Journal.JournalIssue.PubDate.Year.ToString();
                        }
                        catch
                        {
                            stryear = "";
                        }
                        try
                        {
                            strmonth = data.Article.Journal.JournalIssue.PubDate.Month.ToString();
                        }
                        catch
                        {
                            strmonth = "";
                        }
                        try
                        {
                            strday = data.Article.Journal.JournalIssue.PubDate.Day.ToString();
                        }
                        catch
                        {
                            strday = "01";
                        }

                        try
                        {
                            strtitle = data.Article.Journal.Title.ToString();
                        }
                        catch
                        {
                            strtitle = "";
                        }
                        
                        try
                        {
                            strCountry = data.MedlineJournalInfo.Country.ToString();
                        }
                        catch
                        {
                            strCountry = "";
                        }

                        try
                        {
                            strLinktoPubmed = "https://www.ncbi.nlm.nih.gov/pubmed/"+ data.PMID.Text.ToString();
                        }
                        catch
                        {
                            strLinktoPubmed = "";
                        }

                       
                        DBContext.Pubmed_Medlinecitation.Add(new Pubmed_Medlinecitation()
                        {
                            PMID = data.PMID.Text != null ? data.PMID.Text : string.Empty,
                            JournalTitle = data.Article != null ? (data.Article.ArticleTitle != null ? (data.Article.ArticleTitle.ToString()) : string.Empty) : string.Empty,
                            Title = strtitle,
                            JournalCountry = strCountry,
                            Pub_month = strmonth,
                            Pub_year = stryear,
                            Pub_day = strday,
                            Pubdate = String.IsNullOrEmpty(strmonth) ? stryear : String.Join("-", strday,strmonth, stryear),
                            LinktoPubmed= strLinktoPubmed,
                            CreatedDate =DateTime.Now
                        });
                        DBContext.SaveChanges();
                        medlineLastid = DBContext.Pubmed_Medlinecitation.OrderByDescending(x => x.ID).Select(x => x.ID).FirstOrDefault();
                        
                        if (data.Article != null && data.Article.AuthorList != null)
                        {
                            dynamic varAuthorList;
                            try { varAuthorList = data.Article.AuthorList.Author; }
                            catch { varAuthorList = null; }

                            if (varAuthorList != null)
                            {
                                foreach (var cAuth in varAuthorList)
                                {
                                    DBContext.Pubmed_author.Add(new Pubmed_author()
                                    {
                                        Medlinecitation_id = medlineLastid,
                                        authfore = cAuth.ForeName != null ? cAuth.ForeName : "",
                                        authinit = cAuth.Initials != null ? cAuth.Initials : "",
                                        authlast = cAuth.LastName != null ? cAuth.LastName : "",
                                        validyn = cAuth.ValidYN != null ? cAuth.ValidYN : "",
                                        CreatedDate = DateTime.Now
                                    });
                                    DBContext.SaveChanges();
                                    

                                }
                            }
                        }
                        
                        ///AbstratctText
                        if (data.Article != null && data.Article.Abstract != null)
                        {
                            dynamic varAbstract;
                            try
                            {
                                varAbstract = data.Article.Abstract.AbstractText;
                            }
                            catch
                            {
                                varAbstract = null;
                            }
                            if (varAbstract != null)
                            {
                                foreach (var Abs in varAbstract)
                                {
                                    DBContext.Pubmed_Abstracttext.Add(new Pubmed_Abstracttext()
                                    {
                                        Medlinecitation_id = medlineLastid,
                                        abstracttext = Abs.Text != null ? Abs.Text : "",
                                        label = Abs.Label != null ? Abs.Label : "",
                                        nlmcategory = Abs.NlmCategory != null ? Abs.NlmCategory : "",
                                        CreatedDate = DateTime.Now
                                    });
                                    DBContext.SaveChanges();
                                }
                            }
                        }

                        if (data.MeshHeadingList != null)
                        {
                            dynamic varMeshHeadingList = "";

                            try
                            {
                                varMeshHeadingList = data.MeshHeadingList.MeshHeading;
                            }
                            catch
                            {
                                varMeshHeadingList = null;
                            }

                            if (varMeshHeadingList != null)
                            {
                                foreach (var cMesh in varMeshHeadingList)
                                {
                                    var strdescriptorname = "";
                                    var strmajortopicyn = "";
                                    var strui = "";
                                    try
                                    {
                                        strdescriptorname = cMesh.DescriptorName.Text;
                                    }
                                    catch
                                    {
                                        strdescriptorname = "";
                                    }
                                    try
                                    {
                                        strmajortopicyn = cMesh.DescriptorName.MajorTopicYN;
                                    }
                                    catch
                                    {
                                        strmajortopicyn = "";
                                    }
                                    try
                                    {
                                        strui = cMesh.DescriptorName.UI;
                                    }
                                    catch
                                    {
                                        strui = "";
                                    }

                                    DBContext.Pubmed_meshheading.Add(new Pubmed_meshheading()
                                    {
                                        Medlinecitation_id = medlineLastid,
                                        descriptorname = strdescriptorname,
                                        majortopicyn = strmajortopicyn,
                                        // [type],  not in xml but in table
                                        ui = strui,
                                        CreatedDate = DateTime.Now
                                    });
                                    DBContext.SaveChanges();
                                   
                                }
                            }
                        }
                    }
                }
                fs.Close();
                Err.ErrorLog("PubMed xml data inserted into tables completed successfully.");
            }
            catch (Exception ex)
            {
                CreateLogFiles Err = new CreateLogFiles();
                Err.ErrorLog(ex.ToString());
            }
        }

        public class CreateLogFiles
        {
            private string sLogFormat;
            private string sErrorTime;
            private string SavePath;

            public CreateLogFiles()
            {
                sLogFormat = DateTime.Now.ToShortDateString().ToString() + " " + DateTime.Now.ToLongTimeString().ToString() + " ==> ";
                SavePath = "LogFile";/*ConfigurationManager.AppSettings["LogFilepath"].ToString();*/
                sErrorTime = DateTime.Now.ToString("yyyy-MM-dd");
            }

            public void ErrorLog(string sErrMsg)
            {
                if (!Directory.Exists(SavePath + @"\" + DateTime.Now.ToString("yyyy-MM-dd") + @"\" + "LogFile"))
                    Directory.CreateDirectory(SavePath + @"\" + DateTime.Now.ToString("yyyy-MM-dd") + @"\" + "LogFile");

                string sPathName = SavePath + @"\" + DateTime.Now.ToString("yyyy-MM-dd") + @"\LogFile\LogFile.txt";
                StreamWriter sw = new StreamWriter(sPathName, true);
                sw.WriteLine(sLogFormat + sErrMsg);
                sw.Flush();
                sw.Close();
            }
        }

    }



    [XmlRoot(ElementName = "PMID")]
    public class PMID
    {
        [XmlAttribute(AttributeName = "Version")]
        public string Version { get; set; }
        [XmlText]
        public string Text { get; set; }
    }

    [XmlRoot(ElementName = "DateRevised")]
    public class DateRevised
    {
        [XmlElement(ElementName = "Year")]
        public string Year { get; set; }
        [XmlElement(ElementName = "Month")]
        public string Month { get; set; }
        [XmlElement(ElementName = "Day")]
        public string Day { get; set; }
    }

    [XmlRoot(ElementName = "ISSN")]
    public class ISSN
    {
        [XmlAttribute(AttributeName = "IssnType")]
        public string IssnType { get; set; }
        [XmlText]
        public string Text { get; set; }
    }

    [XmlRoot(ElementName = "PubDate")]
    public class PubDate
    {
        [XmlElement(ElementName = "Year")]
        public string Year { get; set; }
        [XmlElement(ElementName = "Month")]
        public string Month { get; set; }
        [XmlElement(ElementName = "Day")]
        public string Day { get; set; }

        [XmlElement(ElementName = "MedlineDate")]
        public string MedlineDate { get; set; }

        [XmlElement(ElementName = "Season")]
        public string Season { get; set; }

    }

    [XmlRoot(ElementName = "JournalIssue")]
    public class JournalIssue
    {
        [XmlElement(ElementName = "Volume")]
        public string Volume { get; set; }
        [XmlElement(ElementName = "PubDate")]
        public PubDate PubDate { get; set; }
        [XmlAttribute(AttributeName = "CitedMedium")]
        public string CitedMedium { get; set; }
        [XmlElement(ElementName = "Issue")]
        public string Issue { get; set; }
    }

    [XmlRoot(ElementName = "Journal")]
    public class Journal
    {
        [XmlElement(ElementName = "ISSN")]
        public ISSN ISSN { get; set; }
        [XmlElement(ElementName = "JournalIssue")]
        public JournalIssue JournalIssue { get; set; }
        [XmlElement(ElementName = "Title")]
        public string Title { get; set; }
        [XmlElement(ElementName = "ISOAbbreviation")]
        public string ISOAbbreviation { get; set; }
    }

    [XmlRoot(ElementName = "Pagination")]
    public class Pagination
    {
        [XmlElement(ElementName = "MedlinePgn")]
        public string MedlinePgn { get; set; }
    }

    [XmlRoot(ElementName = "ELocationID")]
    public class ELocationID
    {
        [XmlAttribute(AttributeName = "EIdType")]
        public string EIdType { get; set; }
        [XmlAttribute(AttributeName = "ValidYN")]
        public string ValidYN { get; set; }
        [XmlText]
        public string Text { get; set; }
    }


    [XmlRoot(ElementName = "Language")]
    public class Language
    {
        [XmlText]
        public string Text { get; set; }
    }

    [XmlRoot(ElementName = "Abstract")]
    public class Abstract
    {
        [XmlElement(ElementName = "CopyrightInformation")]
        public string CopyrightInformation { get; set; }
        [XmlElement(ElementName = "AbstractText")]
        public List<AbstractText> AbstractText { get; set; }
    }

    [XmlRoot(ElementName = "AffiliationInfo")]
    public class AffiliationInfo
    {
        [XmlElement(ElementName = "Affiliation")]
        public string Affiliation { get; set; }
    }

    [XmlRoot(ElementName = "AccessionNumberList")]
    public class AccessionNumberList
    {
        [XmlElement(ElementName = "AccessionNumber")]
        public List<AccessionNumber> AccessionNumber { get; set; }
    }


    [XmlRoot(ElementName = "AccessionNumber")]
    public class AccessionNumber
    {
        [XmlText]
        public string Text { get; set; }
    }


    [XmlRoot(ElementName = "DataBank")]
    public class DataBank
    {
        [XmlElement(ElementName = "DataBankName")]
        public string DataBankName { get; set; }
        [XmlElement(ElementName = "AccessionNumberList")]
        public AccessionNumberList AccessionNumberList { get; set; }
    }

    [XmlRoot(ElementName = "DataBankList")]
    public class DataBankList
    {
        [XmlElement(ElementName = "DataBank")]
        public List<DataBank> DataBank { get; set; }
        [XmlAttribute(AttributeName = "CompleteYN")]
        public string CompleteYN { get; set; }
    }


    [XmlRoot(ElementName = "Author")]
    public class Author
    {
        [XmlElement(ElementName = "LastName")]
        public string LastName { get; set; }
        [XmlElement(ElementName = "ForeName")]
        public string ForeName { get; set; }
        [XmlElement(ElementName = "Initials")]
        public string Initials { get; set; }
        [XmlElement(ElementName = "AffiliationInfo")]
        public List<AffiliationInfo> AffiliationInfo { get; set; }
        [XmlAttribute(AttributeName = "ValidYN")]
        public string ValidYN { get; set; }
        [XmlElement(ElementName = "Identifier")]
        public Identifier Identifier { get; set; }
        [XmlElement(ElementName = "Suffix")]
        public string Suffix { get; set; }
        [XmlElement(ElementName = "CollectiveName")]
        public string CollectiveName { get; set; }
    }

    [XmlRoot(ElementName = "AuthorList")]
    public class AuthorList
    {
        [XmlElement(ElementName = "Author")]
        public List<Author> Author { get; set; }
        [XmlAttribute(AttributeName = "CompleteYN")]
        public string CompleteYN { get; set; }
    }

    [XmlRoot(ElementName = "PublicationType")]
    public class PublicationType
    {
        [XmlAttribute(AttributeName = "UI")]
        public string UI { get; set; }
        [XmlText]
        public string Text { get; set; }
    }

    [XmlRoot(ElementName = "PublicationTypeList")]
    public class PublicationTypeList
    {
        [XmlElement(ElementName = "PublicationType")]
        public List<PublicationType> PublicationType { get; set; }
    }

    [XmlRoot(ElementName = "ArticleDate")]
    public class ArticleDate
    {
        [XmlElement(ElementName = "Year")]
        public string Year { get; set; }
        [XmlElement(ElementName = "Month")]
        public string Month { get; set; }
        [XmlElement(ElementName = "Day")]
        public string Day { get; set; }
        [XmlAttribute(AttributeName = "DateType")]
        public string DateType { get; set; }
    }

    [XmlRoot(ElementName = "Article")]
    public class Article
    {
        [XmlElement(ElementName = "Journal")]
        public Journal Journal { get; set; }
        [XmlElement(ElementName = "Pagination")]
        public Pagination Pagination { get; set; }
        [XmlElement(ElementName = "ELocationID")]
        public List<ELocationID> ELocationID { get; set; }

        [XmlElement(ElementName = "Abstract")]
        public Abstract Abstract { get; set; }
        [XmlElement(ElementName = "AuthorList")]
        public AuthorList AuthorList { get; set; }

        [XmlElement(ElementName = "Language")]
        public List<Language> Language { get; set; }

        [XmlElement(ElementName = "PublicationTypeList")]
        public PublicationTypeList PublicationTypeList { get; set; }
        [XmlElement(ElementName = "ArticleDate")]
        public ArticleDate ArticleDate { get; set; }
        [XmlAttribute(AttributeName = "PubModel")]
        public string PubModel { get; set; }

        [XmlElement(ElementName = "ArticleTitle")]
        // public string ArticleTitle { get; set; }
        public string ArticleTitle { get; set; }

        [XmlElement(ElementName = "GrantList")]
        public GrantList GrantList { get; set; }

        [XmlElement(ElementName = "VernacularTitle")]
        // public string ArticleTitle { get; set; }
        public string VernacularTitle { get; set; }


    }

    [XmlRoot(ElementName = "MedlineJournalInfo")]
    public class MedlineJournalInfo
    {
        [XmlElement(ElementName = "Country")]
        public string Country { get; set; }

        [XmlElement(ElementName = "MedlineTA")]
        public string MedlineTA { get; set; }
        [XmlElement(ElementName = "NlmUniqueID")]
        public string NlmUniqueID { get; set; }
        [XmlElement(ElementName = "ISSNLinking")]
        public string ISSNLinking { get; set; }
    }

    [XmlRoot(ElementName = "Keyword")]
    public class Keyword
    {
        [XmlAttribute(AttributeName = "MajorTopicYN")]
        public string MajorTopicYN { get; set; }
        [XmlText]
        public string Text { get; set; }
    }

    [XmlRoot(ElementName = "KeywordList")]
    public class KeywordList
    {
        [XmlElement(ElementName = "Keyword")]
        public List<Keyword> Keyword { get; set; }
        [XmlAttribute(AttributeName = "Owner")]
        public string Owner { get; set; }
    }


    [XmlRoot(ElementName = "SupplMeshList")]
    public class SupplMeshList
    {
        [XmlElement(ElementName = "SupplMeshName")]
        public List<SupplMeshName> SupplMeshName { get; set; }

    }


    [XmlRoot(ElementName = "SupplMeshName")]
    public class SupplMeshName
    {
        [XmlAttribute(AttributeName = "UI")]
        public string UI { get; set; }

        [XmlAttribute(AttributeName = "Type")]
        public string Type { get; set; }

        [XmlText]
        public string Text { get; set; }
    }


    [XmlRoot(ElementName = "OtherAbstract")]
    public class OtherAbstract
    {
        [XmlElement(ElementName = "AbstractText")]
        public List<OtherAbstractText> AbstractText { get; set; }

        [XmlAttribute(AttributeName = "Type")]
        public string Type { get; set; }

        [XmlAttribute(AttributeName = "Language")]
        public string Language { get; set; }

    }


    [XmlRoot(ElementName = "OtherAbstractText")]
    public class OtherAbstractText
    {
        [XmlAttribute(AttributeName = "Label")]
        public string Label { get; set; }

        [XmlAttribute(AttributeName = "NlmCategory")]
        public string NlmCategory { get; set; }

        [XmlText]
        public string Text { get; set; }
    }

    [XmlRoot(ElementName = "Investigator")]
    public class Investigator
    {
        [XmlElement(ElementName = "LastName")]
        public string LastName { get; set; }
        [XmlElement(ElementName = "ForeName")]
        public string ForeName { get; set; }
        [XmlElement(ElementName = "Initials")]
        public string Initials { get; set; }
        [XmlAttribute(AttributeName = "ValidYN")]
        public string ValidYN { get; set; }
    }

    [XmlRoot(ElementName = "InvestigatorList")]
    public class InvestigatorList
    {
        [XmlElement(ElementName = "Investigator")]
        public List<Investigator> Investigator { get; set; }
    }


    [XmlRoot(ElementName = "MedlineCitation")]
    public class MedlineCitation
    {
        [XmlElement(ElementName = "PMID")]
        public PMID PMID { get; set; }
        [XmlElement(ElementName = "DateRevised")]
        public DateRevised DateRevised { get; set; }
        [XmlElement(ElementName = "Article")]
        public Article Article { get; set; }

        [XmlElement(ElementName = "DataBankList")]
        public DataBankList DataBankList { get; set; }

        [XmlElement(ElementName = "MedlineJournalInfo")]

        public MedlineJournalInfo MedlineJournalInfo { get; set; }

        [XmlElement(ElementName = "KeywordList")]
        public KeywordList KeywordList { get; set; }

        [XmlElement(ElementName = "InvestigatorList")]
        public InvestigatorList InvestigatorList { get; set; }


        [XmlElement(ElementName = "SupplMeshList")]
        public SupplMeshList SupplMeshList { get; set; }

        [XmlElement(ElementName = "OtherAbstract")]
        public OtherAbstract OtherAbstract { get; set; }

        [XmlAttribute(AttributeName = "Status")]
        public string Status { get; set; }
        [XmlAttribute(AttributeName = "Owner")]
        public string Owner { get; set; }
        [XmlElement(ElementName = "CommentsCorrectionsList")]
        public CommentsCorrectionsList CommentsCorrectionsList { get; set; }

        [XmlElement(ElementName = "DateCompleted")]
        public DateCompleted DateCompleted { get; set; }

        [XmlElement(ElementName = "CitationSubset")]
        public List<CitationSubset> CitationSubset { get; set; }

        [XmlElement(ElementName = "MeshHeadingList")]
        public MeshHeadingList MeshHeadingList { get; set; }
        [XmlElement(ElementName = "CoiStatement")]
        public string CoiStatement { get; set; }
        [XmlElement(ElementName = "ChemicalList")]
        public ChemicalList ChemicalList { get; set; }
    }


    [XmlRoot(ElementName = "CitationSubset")]
    public class CitationSubset
    {
        [XmlText]
        public string Text { get; set; }
    }

    [XmlRoot(ElementName = "PubMedPubDate")]
    public class PubMedPubDate
    {
        [XmlElement(ElementName = "Year")]
        public string Year { get; set; }
        [XmlElement(ElementName = "Month")]
        public string Month { get; set; }
        [XmlElement(ElementName = "Day")]
        public string Day { get; set; }
        [XmlAttribute(AttributeName = "PubStatus")]
        public string PubStatus { get; set; }
        [XmlElement(ElementName = "Hour")]
        public string Hour { get; set; }
        [XmlElement(ElementName = "Minute")]
        public string Minute { get; set; }
    }

    [XmlRoot(ElementName = "History")]
    public class History
    {
        [XmlElement(ElementName = "PubMedPubDate")]
        public List<PubMedPubDate> PubMedPubDate { get; set; }
    }

    [XmlRoot(ElementName = "ArticleId")]
    public class ArticleId
    {
        [XmlAttribute(AttributeName = "IdType")]
        public string IdType { get; set; }
        [XmlText]
        public string Text { get; set; }
    }

    [XmlRoot(ElementName = "ArticleIdList")]
    public class ArticleIdList
    {
        [XmlElement(ElementName = "ArticleId")]
        public List<ArticleId> ArticleId { get; set; }
    }

    [XmlRoot(ElementName = "PubmedData")]
    public class PubmedData
    {
        [XmlElement(ElementName = "History")]
        public History History { get; set; }
        [XmlElement(ElementName = "PublicationStatus")]
        public string PublicationStatus { get; set; }
        [XmlElement(ElementName = "ArticleIdList")]
        public ArticleIdList ArticleIdList { get; set; }
    }

    [XmlRoot(ElementName = "PubmedArticle")]
    public class PubmedArticle
    {
        [XmlElement(ElementName = "MedlineCitation")]
        public MedlineCitation MedlineCitation { get; set; }
        [XmlElement(ElementName = "PubmedData")]
        public PubmedData PubmedData { get; set; }
    }

    [XmlRoot(ElementName = "AbstractText")]
    public class AbstractText
    {

        [XmlAttribute(AttributeName = "Label")]
        public string Label { get; set; }
        [XmlAttribute(AttributeName = "NlmCategory")]
        public string NlmCategory { get; set; }
        [XmlText]
        public string Text { get; set; }
        //[XmlElement(ElementName = "i")]
        //public I I { get; set; }
    }

    //[XmlRoot(ElementName = "ArticleTitle")]
    //public class ArticleTitle
    //{
    //    [XmlElement(ElementName = "sup")]
    //    public string Sup { get; set; }
    //}

    [XmlRoot(ElementName = "Identifier")]
    public class Identifier
    {
        [XmlAttribute(AttributeName = "Source")]
        public string Source { get; set; }
        [XmlText]
        public string Text { get; set; }
    }

    [XmlRoot(ElementName = "Grant")]
    public class Grant
    {
        [XmlElement(ElementName = "GrantID")]
        public string GrantID { get; set; }
        [XmlElement(ElementName = "Acronym")]
        public string Acronym { get; set; }
        [XmlElement(ElementName = "Agency")]
        public string Agency { get; set; }
        [XmlElement(ElementName = "Country")]
        public string Country { get; set; }
    }

    [XmlRoot(ElementName = "GrantList")]
    public class GrantList
    {
        [XmlElement(ElementName = "Grant")]
        public List<Grant> Grant { get; set; }
        [XmlAttribute(AttributeName = "CompleteYN")]
        public string CompleteYN { get; set; }
    }

    [XmlRoot(ElementName = "CommentsCorrections")]
    public class CommentsCorrections
    {
        [XmlElement(ElementName = "RefSource")]
        public string RefSource { get; set; }
        [XmlElement(ElementName = "PMID")]
        public PMIDCorrection PMID { get; set; }
        [XmlAttribute(AttributeName = "RefType")]
        public string RefType { get; set; }
    }

    [XmlRoot(ElementName = "PMIDCorrection")]
    public class PMIDCorrection
    {
        [XmlAttribute(AttributeName = "Version")]
        public string Version { get; set; }
        [XmlText]
        public string Text { get; set; }
    }



    [XmlRoot(ElementName = "CommentsCorrectionsList")]
    public class CommentsCorrectionsList
    {
        [XmlElement(ElementName = "CommentsCorrections")]
        public List<CommentsCorrections> CommentsCorrections { get; set; }
    }

    [XmlRoot(ElementName = "DateCompleted")]
    public class DateCompleted
    {
        [XmlElement(ElementName = "Year")]
        public string Year { get; set; }
        [XmlElement(ElementName = "Month")]
        public string Month { get; set; }
        [XmlElement(ElementName = "Day")]
        public string Day { get; set; }
    }

    [XmlRoot(ElementName = "DescriptorName")]
    public class DescriptorName
    {
        [XmlAttribute(AttributeName = "UI")]
        public string UI { get; set; }
        [XmlAttribute(AttributeName = "MajorTopicYN")]
        public string MajorTopicYN { get; set; }
        [XmlText]
        public string Text { get; set; }
    }

    [XmlRoot(ElementName = "QualifierName")]
    public class QualifierName
    {
        [XmlAttribute(AttributeName = "UI")]
        public string UI { get; set; }
        [XmlAttribute(AttributeName = "MajorTopicYN")]
        public string MajorTopicYN { get; set; }
        [XmlText]
        public string Text { get; set; }
    }

    [XmlRoot(ElementName = "MeshHeading")]
    public class MeshHeading
    {
        [XmlElement(ElementName = "DescriptorName")]
        public DescriptorName DescriptorName { get; set; }
        [XmlElement(ElementName = "QualifierName")]
        public List<QualifierName> QualifierName { get; set; }
    }

    [XmlRoot(ElementName = "MeshHeadingList")]
    public class MeshHeadingList
    {
        [XmlElement(ElementName = "MeshHeading")]
        public List<MeshHeading> MeshHeading { get; set; }
    }

    [XmlRoot(ElementName = "NameOfSubstance")]
    public class NameOfSubstance
    {
        [XmlAttribute(AttributeName = "UI")]
        public string UI { get; set; }
        [XmlText]
        public string Text { get; set; }
    }

    [XmlRoot(ElementName = "Chemical")]
    public class Chemical
    {
        [XmlElement(ElementName = "RegistryNumber")]
        public string RegistryNumber { get; set; }
        [XmlElement(ElementName = "NameOfSubstance")]
        public NameOfSubstance NameOfSubstance { get; set; }
    }

    [XmlRoot(ElementName = "ChemicalList")]
    public class ChemicalList
    {
        [XmlElement(ElementName = "Chemical")]
        public List<Chemical> Chemical { get; set; }
    }

    [XmlRoot(ElementName = "i")]
    public class I
    {
        [XmlElement(ElementName = "sub")]
        public string Sub { get; set; }
    }

    [XmlRoot(ElementName = "PubmedArticleSet")]
    public class PubmedArticleSet
    {
        [XmlElement(ElementName = "PubmedArticle")]
        public List<PubmedArticle> PubmedArticle { get; set; }
    }

}