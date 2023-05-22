"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation() научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""


import logging
from datetime import *
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

 
def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)
    
def planets(command):
    nowdate = str(date.today())
    nowdate = nowdate.replace('-', '/')
    planet = command.replace('/planet ', '')
    if planet == 'Mars':
        E_planet = ephem.Mars(nowdate)
    elif planet == 'Mercury':
        E_planet = ephem.Mercury(nowdate)
    elif planet == 'Venus':
        E_planet = ephem.Venus(nowdate)
    elif planet == 'Jupiter':
        E_planet = ephem.Jupiter(nowdate) 
    elif planet == 'Saturn':
        E_planet = ephem.Saturn(nowdate)
    elif planet == 'Uranus':
        E_planet = ephem.Uranus(nowdate)
    elif planet == 'Neptune':
        E_planet = ephem.Neptune(nowdate)   
    
    const = ephem.constellation(E_planet)
    return(const)
 

def talk_to_me(update, context):
    nowdate = str(date.today())  
    nowdate = nowdate.replace('-', '/')
    user_text= update.message.text
    if '/planet' in user_text:
      result = planets(user_text)
      update.message.reply_text(result)  
    print(user_text)

def main():
    mybot = Updater("6288224045:AAFbJty0fKY_vz_lrTeEp3vZ4jyePiECfxg", use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
