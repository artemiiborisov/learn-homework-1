"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

from itertools import count

phones = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]
def main():
     """
     Эта функция вызывается автоматически при запуске скрипта в консоли
     В ней надо заменить pass на ваш код
     """

def count_avg(my_list):
    sold_avg = sum(my_list) / len(my_list)
    return sold_avg


for one_product in phones:
    product_avg_sold = count_avg(one_product['items_sold'])
    print(f"Среднее количество продаж для товара {one_product['product']}: {product_avg_sold}")

avg_sold_sum = []
for one_product in phones:
    avg_sold_sum.append(count_avg(one_product['items_sold']))
phones_avg = count_avg(avg_sold_sum)
print(f"Среднее количество продаж всех товаров {phones_avg}")

def count_avg(phones_sold):
    summary = sum(phones_sold)
    return summary

month_counter = 0
for one_product in phones:
    product_sold = count_avg(one_product['items_sold'])
    print(f"Сумма продаж для товара {one_product['product']}: {product_sold}")

avg_sold_sum = 0
for one_product in phones:
    avg_sold_sum += count_avg(one_product['items_sold'])
phones_avg = avg_sold_sum
print(f"Сумма продаж всех товаров {phones_avg}")

if __name__ == "__main__":
     main()