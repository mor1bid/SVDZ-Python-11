import time
import getpass

# 1
class Mystr(str):
    _spy = '\nhi, ' + getpass.getuser() + ' its ' + str(time.time())
    def __init__(self, inp):
        self.inp = str(inp)
    def res(self):
        return self.inp + self._spy
    def __str__(self):
        res = self.res()
        return res
    
notmynum = Mystr(42)
print(notmynum + ' thats odd')

# 2
class Archive:
    _arcnum = None
    _arcline = None
    _arclist = list()
    # def __new__(cls, *args):
    #     if cls._arcnum != None or cls._arcline != None:
    #         cls._arclist = super().__new__(cls)
    #     return cls._arclist
    def __init__(self, num, line):
        self._arcnum = num
        self._arcline = line
    def __dataret__(self):
        return self._arcnum, self._arcline
    def listapp(self):
        self._arclist.append(self._arcnum)
        self._arclist.append(self._arcline)
        return self._arclist
    def __str__(self):
        work = self.listapp()
        return str(work)
    def __new__(cls, *args):
        if cls._arcnum != None or cls._arcline != None:
            cls._arclist = super().__new__(cls)
        return cls._arclist
    
listalpha = Archive(13, '- чёртовая дюжина')
listbeta = Archive(777, '- джекпот')
print(listalpha)
print(listbeta)