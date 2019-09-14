from bs4 import BeautifulSoup
import re
import urllib
from lxml import etree


class HtmlParser(object):
    def __GetNewUrls(self,pageurl,soup):
        newurls=set()
        dom=etree.HTML(soup)
        links=dom.xpath("//div[@class='para']/a/@href")
        for link in links:
            newfulllink=urllib.parse.urljoin(pageurl,link)
            newurls.add(newfulllink)
        return newurls
    def __GetNewDatas(self,pageurl,soup):
        dom=etree.HTML(soup)
        data={}
        data['url']=pageurl
        title=dom.xpath("//dd[@class='lemmaWgt-lemmaTitle-title']/h1/text()")[0]
        data['title']=dom.xpath("//dd[@class='lemmaWgt-lemmaTitle-title']/h1/text()")[0]
        data['summary']=dom.xpath("//div[@class='lemma-summary']/div[@class='para']/text()")[0]
        return data
    def Parser(self,pageurl,content):
        if pageurl is None or content is None:
            return
        newurls=self.__GetNewUrls(pageurl,content)
        newdata=self.__GetNewDatas(pageurl,content)
        return newurls,newdata