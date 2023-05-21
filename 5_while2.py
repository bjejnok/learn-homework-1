"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""
from datetime import *
nowtime = datetime.now()
nowdate = str(date.today())
nowdate = nowdate.replace('-', '/')

questions_and_answers = {
    "как дела?": "Хорошо!", 
    "что делаешь?": "Программирую",
    "сколько времени?": nowtime.strftime("%H:%M"),
    "какое сегодня число?": nowdate,
    "почем гречка?": "100 рублей за кг",
    "отель?": "Триваго!"
}

def ask_user(answers_dict):
    while True:
      ask = input("Задайте вопрос: ")
      if ask in questions_and_answers:
          answer = questions_and_answers[ask]
      else: answer = "Вопроса нет в списке"   
      print(answer)   

    
if __name__ == "__main__":
    ask_user(questions_and_answers)
