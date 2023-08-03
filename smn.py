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
        """Сохранение полученное значение inp"""
        return self.inp
    def __str__(self):
        """Выводим значение inp на печать"""
        res = self.res()
        return res
    
print('1.:')
notmynum = Mystr(42)
print(notmynum + ' thats odd')
# print('\nСправка класса Mystr ниже', '*' * 50)
# help(Mystr)
print(f'Документация класса: {Mystr.__doc__ = }')
print(f'Документация экземпляра: {notmynum.__doc__ = }')
print(f'Документация метода: {Mystr.res.__doc__ = }')


# 2
class Archive:
    """Класс, принимающий и хранящий числовое и строковое значения, которые добавляет в список"""
    _arcnum = None
    _arcline = None
    _arclist = list()

    def __init__(self, num, line):
        """Получение значений из экземпляра класса"""
        self._arcnum = num
        self._arcline = line
    def __dataret__(self):
        """Сохранение полученных значений"""
        return self._arcnum, self._arcline
    def listapp(self):
        """Добавление значений экземпляра в список"""
        self._arclist.append(self._arcnum)
        self._arclist.append(self._arcline)
        return self._arclist
    def __str__(self):
        """Вывод списка на печать (для пользователя)"""
        work = self.listapp()
        return str(work)
    def __repr__(self):
        """Вывод списка на печать (для программиста)"""
        return f'Archive({self.listapp()})'
    
print('\n2.:')
listalpha = Archive(13, '- чёртовая дюжина')
listbeta = Archive(777, '- джекпот')
print(listalpha)
print(listbeta, '\n')
print(repr(listalpha))
print(repr(listbeta))
print(f'Документация класса: {Archive.__doc__ = }')
print(f'Документация экземпляра: {listalpha.__doc__ = }')
print(f'Документация метода: {Archive.listapp.__doc__ = }')

class Rectan:
    "Класс обработки двух переменных и вычисления площади и периметра четырёхсторонней фигуры"
    def __init__(self, *args, lng = ' ', wdt = ' '):
        "Получение переменных от пользователя"
        self.lng = int(args[0])
        self.wdt = int(args[-1])
    def __str__(self):
        "Вывод результата"
        return f'Площадь = {self.lng * self.wdt}\nПериметр = {2 * (self.lng + self.wdt)}'


print('\n5.:')
paramets = input("5. Введите желаемую длину и ширину прямоугольника через пробел\n: ")
paramets = paramets.split()
ex = Rectan(paramets[0], paramets[-1])
print(ex)
print(f'Документация класса: {Rectan.__doc__ = }')
print(f'Документация экземпляра: {paramets.__doc__ = }')
