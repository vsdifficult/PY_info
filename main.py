from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, Dispatcher, executor, types
from keyboards import start_menu
from dadata import Dadata
from bs4 import BeautifulSoup
from aiogram.dispatcher.filters import Text 

from config import BOT_TOKEN, token, secret
from config_chat import * 

import io, requests

bot = Bot(token=BOT_TOKEN) 
dp = Dispatcher(bot) 

@dp.message_handler(commands=['start']) 
async def send_welcom(message: types.Message): 
    await message.reply(f'Здравствуйте {message.from_user.first_name}, вы пользуетесь ботом для Python разработки', reply_markup=start_menu) 

@dp.message_handler(Text(equals='INFO📕')) 
async def main(message: types.Message):  
    await message.reply(info) 

@dp.message_handler(Text(equals='Бесплатный GPT🥇'))
async def GPT(message: types.Message): 
    await message.reply("https://t.me/GPT2_neuronbot") 

@dp.message_handler(lambda message: message.text == 'Курсы IT🎟') 
async def kyrsa(message: types.Message): 
    kyrs = InlineKeyboardMarkup(row_width=3) 
    btn = InlineKeyboardButton(text= 'GeekBrains', url='https://gb.ru')  
    btn2 = InlineKeyboardButton(text='Яндекс Практикум', callback_data='https://practicum.yandex.ru/catalog/start/') 
    btn3 = InlineKeyboardButton(text = 'SkillFactory', url='https://skillfactory.ru') 
    btn4 = InlineKeyboardButton(text='SkillBOX', url='https://skillbox.ru/code/') 
    kyrs.add(btn, btn2, btn3, btn4)
    await message.reply('Курсы по IT технологиям', reply_markup=kyrs)

@dp.message_handler(lambda message: message.text == 'Доп функции🛠')
async def dopfunc(message: types.Message): 
     buttons = types.ReplyKeyboardMarkup(resize_keyboard=True) 
     ph = types.KeyboardButton(text = 'Parser')  
     bask = types.KeyboardButton(text = 'Назад 🔙') 
     phone_ = types.KeyboardButton(text = 'Phone📞')
     buttons.add(phone, bask, ph, phone_) 
     await message.reply('Выберите функцию', reply_markup=buttons)

@dp.message_handler(Text(equals='Parser')) 
async def pars_mode(message: types.Message): 
    await message.reply('Введите ссылку') 

    @dp.message_handler() 
    async def mes(message: types.Message): 
        data = message.text
        response = requests.get(data) 
        if response.status_code == 200: 
            f = BeautifulSoup(response.text, 'html.parser')
            with io.open('prototip_html_resault.txt', 'w', encoding='utf-8') as S:
                S.write(str(f))
            
            await message.answer_document(open('prototip_html_resault.txt', 'r'))
        elif (response.status_code == 400): 
            await message.reply('Сбой подключения (HTTPerror, URLerror)')

@dp.message_handler(Text(equals='Phone📞')) 
async def phone(message: types.Message): 
      await message.reply('Введите номер телефона') 

      @dp.message_handler() 
      async def msg(message: types.Message): 
          phone_txt = int(message.text)
          dadata = Dadata(token, secret)
          result = dadata.clean("phone", phone_txt) 

          with io.open('phone_info.txt', 'w', encoding='utf-8') as f: 
              f.write(str(result))
              
          await message.reply_document(open('phone_info.txt', 'r'))
@dp.message_handler(Text(equals='Назад 🔙'))  
async def main_t(message: types.Message): 
     text = message.text 
     if text == 'Назад 🔙': 
          await message.reply("Выберите понятие", reply_markup=start_menu)

@dp.message_handler(lambda message: message.text == 'Основные понятия Python🧧') 
async def main_c(message: types.Message): 
     btn___ = types.ReplyKeyboardMarkup(resize_keyboard=True) 
     peremenn = types.KeyboardButton(text = 'Переменные') 
     sync = types.KeyboardButton(text = 'Синхронизация')
     func = types.KeyboardButton(text = 'Функции')
     class_meth = types.KeyboardButton(text = 'Классы и методы')
     lib = types.KeyboardButton(text = 'Библиотеки')
     back = types.KeyboardButton(text = 'Назад 🔙') 
     btn___.add(peremenn, func, back, lib, class_meth, sync)  
     await message.reply("Выберите понятие", reply_markup=btn___) 


@dp.message_handler(Text(equals='Переменные')) 
async def main_a(message: types.Message): 
    await message.reply(py_pereme)
    
@dp.message_handler(Text(equals='Функции')) 
async def func(message: types.Message): 
    await message.reply(funct) 

@dp.message_handler(Text(equals='Синхронизация'))
async def senc(message: types.Message): 
    await message.reply(sync)

@dp.message_handler(Text(equals='Библиотеки'))
async def lib_(message: types.Message): 
    await message.reply(lib__)

@dp.message_handler(Text(equals='Классы и методы'))
async def lib3(message: types.Message): 
    await message.reply(objclasss)

@dp.message_handler(Text(equals='Назад 🔙'))  
async def main_t(message: types.Message): 
     text = message.text 
     if text == 'Назад 🔙': 
          await message.reply("Выберите понятие", reply_markup=start_menu)
          
if __name__ == '__main__': 
    executor.start_polling(dp, skip_updates=True)