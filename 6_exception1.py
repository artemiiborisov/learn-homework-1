"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

hello_user = input('Как дела? ')
while True:
        try:
            if hello_user == 'Хорошо':
                print('Прекрасно')
        except KeyboardInterrupt:
            print('Пока')
            break