"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""



def hello_user():
     """
     Замените pass на ваш код
     """

 
while True:   
    try:
        hello_user_input = input('Как дела? ')
        if hello_user_input == 'Хорошо':
            print('Прекрасно')
    except KeyboardInterrupt:
        print("Ну напиши уже 'Хорошо'")
        break
if __name__ == "__main__":
    hello_user()