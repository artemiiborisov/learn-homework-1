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

def main():
     """
     Эта функция вызывается автоматически при запуске скрипта в консоли
     В ней надо заменить pass на ваш код
     """

def compare_str(string1, string2):
    if type(string1) != str or type(string2) != str :
        return 0
    elif string1 == string2:
        return 1
    elif string1 != string2 and string2 == 'learn':
        return 3
    elif string1 != string2 and len(string1) > len(string2):
        return 2
    elif string1 != string2 and len(string1) < len(string2):
        return 4

string1, string2 = input('Введите текст1'), input('Введите текст2')
print(compare_str(string1, string2))

if __name__ == "__main__":
     main()