
import base64
class changeWorker:
    def thunderToNormal(self,url):
        if url.startswith('thunder://')or url.startswith('Thunder://'):
            mystr = url[10:]
        else:
            mystr = url
        mystr =  bytes(mystr, encoding = "utf8")
        missing_padding = 4 - len(url) % 4
        if missing_padding:
            mystr += b'=' * missing_padding
        mystr2 = base64.decodebytes(mystr)
        #result = str(mystr2,'utf-8')
        result = mystr2.decode()
        return result[2:-2]
 
 
mychangeWorker = changeWorker()
while 1:
    mystr = input('input thunder URL')
    print(mychangeWorker.thunderToNormal(mystr))