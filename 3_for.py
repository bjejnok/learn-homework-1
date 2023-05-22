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
iphone = {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}
xiaomi = {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]}
samsung = {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]}

def summ(product_name):
    sum = 0
    length = len(product_name['items_sold'])
    for i in range(length):
        sum += product_name['items_sold'][i]
    return(sum)

def medium(product_name):
    medium = summ(product_name) / len(product_name['items_sold'])
    return(medium) 

def total_sum(*args):
    sum = 0
    for i in args:
        sum += summ(i)
    return(sum)


def total_medium(*args):
    total_length = 0
    for i in args:
        total_length += len(i['items_sold'])
    total_medium = total_sum(*args) / total_length
    return(total_medium)


def main():
    print(summ(iphone))
    print(summ(xiaomi))
    print(summ(samsung))
    
    print(medium(iphone))
    print(medium(xiaomi))
    print(medium(samsung))
    
    print(total_sum(iphone, xiaomi, samsung))
    print(total_medium(iphone, xiaomi, samsung))

if __name__ == "__main__":
    main()
