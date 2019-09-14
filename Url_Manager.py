class UrlManager(object):
    def __init__(self):
        self.new_urls=set()
        self.old_urls=set()
    def AddNewUrl(self,url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def AddNewUrls(self,urls):
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.AddNewUrl(url)
    def HasNewUrl(self):
        return len(self.new_urls)!=0
    def GetNewUrl(self):
        newurl=self.new_urls.pop()
        self.old_urls.add(newurl)
        return newurl
    def GetOldUrlSize(self):
        return len(self.old_urls)