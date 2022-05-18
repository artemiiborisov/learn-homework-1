"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
def compare_str(stroka1, stroka2):
  if type(stroka1) != str and type(stroka1) != str :
    return 0
  elif stroka1 == stroka2:
    return 1
  elif stroka1 != stroka2 and stroka2 == 'learn':
    return 3
  elif stroka1 != stroka2 and len(stroka1) > len(stroka2):
    return 2

stroka1, stroka2 = input(), input()
print(compare_str(stroka1, stroka2))
