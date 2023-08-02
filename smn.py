from datetime import datetime
import getpass

# 1
class Mystr(str):
    """Модифицированный класс str, с дополнительно хранящимися именем автора вводимой строки и временем её создания"""
    _spy = '\nhi, ' + getpass.getuser() + ' its ' + datetime.now().strftime("%H:%M")
    def __init__(self, inp):
        """Конвертируем принятое значение inp и выводим вместе с ним данные о пользователе и времени обращения"""
        print(self._spy)
        self.inp = str(inp)
    def res(self):
        """Возвращаем полученное значение inp"""
        return self.inp
    def __str__(self):
        """Выводим значение inp на печать"""
        res = self.res()
        return res
    
notmynum = Mystr(42)
print(notmynum + ' thats odd')
# print('\nСправка класса Mystr ниже', '*' * 50)
# help(Mystr)
print(f'1.:\n Документация класса: {Mystr.__doc__ = }')
print(f'Документация экземпляра: {notmynum.__doc__ = }')
print(f'Документация метода: {Mystr.res.__doc__ = }')


# 2
class Archive:
    """Класс, принимающий и хранящий числовое и строковое значения, которые добавляет в список"""
    _arcnum = None
    _arcline = None
    _arclist = list()
    # def __new__(cls, *args):
    #     if cls._arcnum != None or cls._arcline != None:
    #         cls._arclist = super().__new__(cls)
    #     else:
    #         return cls._arclist
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
    
listalpha = Archive(13, '- чёртовая дюжина')
listbeta = Archive(777, '- джекпот')
print(listalpha)
print(listbeta)