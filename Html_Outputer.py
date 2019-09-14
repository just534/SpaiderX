import codecs
class DataOutPut(object):
    def __init__(self):
        self.datas=[]
    def StoreData(self,data):
        if data is None:
            return
        self.datas.append(data)
    def OutPut(self):
        print(self.datas)