import requests
class HtmlDownload(object):
    def Download(self,url):
        if url is None:
            return None
        header={
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
            "Refere":"https://baike.baidu.com/search/none?word=%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB%E9%99%AA%E4%BD%A0%E8%BF%87&pn=0&rn=10&enc=utf8"
        }
        resp=requests.get(url,headers=header)
        if resp.status_code!=200:
            return
        return resp.content.decode()