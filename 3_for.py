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

phones = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

def count_sum(phones_sold):
  summary = 0
  for sold in phones_sold:
    summary += sold
  sold_avg = summary / len(phones_sold)
  return sold_avg
for one_product in phones:
  product_avg_sold = count_sum(one_product['items_sold'])
  print(f"Среднее количество продаж для товара {one_product['product']}: {product_avg_sold}")



avg_sold_sum = 0
for one_product in phones:
  avg_sold_sum += count_sum(one_product['items_sold'])
phones_avg = avg_sold_sum / len(phones)
print(f"Среднее количество продаж всех товаров {phones_avg}")

def count_sum(phones_sold):
  summary = 0
  for sold in phones_sold:
    summary += sold
  return summary

month_counter = 0
for one_product in phones:
  product_sold = count_sum(one_product['items_sold'])
  print(f"Сумма продаж для товара {one_product['product']}: {product_sold}")

avg_sold_sum = 0
for one_product in phones:
  avg_sold_sum += count_sum(one_product['items_sold'])
phones_avg = avg_sold_sum
print(f"Сумма продаж всех товаров {phones_avg}")