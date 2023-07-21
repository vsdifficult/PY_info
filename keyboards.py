from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message, InlineKeyboardMarkup, InlineKeyboardButton

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            
            KeyboardButton(text = 'INFO📕')
            
        ], 
        [
           KeyboardButton(text = 'Основные понятия Python🧧')
        ], 
        
        [
            KeyboardButton(text= 'Бесплатный GPT🥇')
        ], 
        [
            KeyboardButton(text= 'Курсы IT🎟')
        ] 
        
    ], resize_keyboard=True
) 

kyrs = InlineKeyboardMarkup(
    inline_keyboard=[
         [
             InlineKeyboardButton(text='SkillBOX', url='https://skillbox.ru/code/')
         ], 
         [
             InlineKeyboardButton(text = 'SkillFactory', url='https://skillfactory.ru')
         ], 
         [
             InlineKeyboardButton(text='Яндекс Практикум', callback_data='https://practicum.yandex.ru/catalog/start/') 
         ], 
         [
             InlineKeyboardButton(text= 'GeekBrains', url='https://gb.ru')
         ]
    ], row_width=1
)
