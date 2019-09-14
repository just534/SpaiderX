import Url_Manager
import Html_Downloader
import Html_Parser
import Html_Outputer
class SpaiderMain(object):
    def __init__(self):
        self.urlmanager=Url_Manager.UrlManager()
        self.htmdownloader=Html_Downloader.HtmlDownload()
        self.htmlparser=Html_Parser.HtmlParser()
        self.htmoutput=Html_Outputer.DataOutPut()
    def Crawl(self,rooturl):
        self.urlmanager.AddNewUrl(rooturl)
        while(self.urlmanager.HasNewUrl() and self.urlmanager.GetOldUrlSize()<500):
            try:
                newurl=self.urlmanager.GetNewUrl()
                html=self.htmdownloader.Download(newurl)
                newurls,data=self.htmlparser.Parser(newurl,html)
                self.urlmanager.AddNewUrls(newurls)
                self.htmoutput.StoreData(data)
                print("已抓取%s个链接"%self.urlmanager.GetOldUrlSize())
            except Exception:
                print("crawl failed!")
        self.htmoutput.OutPut()




if __name__=='__main__':
    sp=SpaiderMain()
    sp.Crawl("https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB")
