from random import choice, random
import telebot
from telebot.types import KeyboardButton

TOKEN='7157043888:AAGQT2eWN13Ntu3HWvHjzNuGZxZW7nsoh9k'
bot=telebot.TeleBot(TOKEN)

def generate_random_card():
    CARD_NUMBER = ['6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']
    CARD_SUIT = ['Черви', 'Бубны', 'Пики', 'Трефы']
    random_card_number=choice(CARD_NUMBER)
    random_card_suit=choice(CARD_SUIT)
    return random_card_number, random_card_suit

def easy_compare_message(message):
    card_number, card_suit=generate_random_card()
    if message.text == "🟥" and card_suit in ['Черви', 'Бубны']:
        bot.send_message(message.chat.id,'Верно! Карта, которую я загадал '+ card_number + '-' + card_suit)
    elif message.text == "⬛️" and card_suit in ['Пики', 'Трефы']:
        bot.send_message(message.chat.id,'Верно! Карта, которую я загадал ' + card_number + '-' + card_suit)
    else:
        bot.send_message(message.chat.id, 'Не повезло! Эта карта была ' + card_number + '-' + card_suit)

def mid_compare_message(message):
    card_number, card_suit = generate_random_card()
    if message.text == card_suit:
        bot.send_message(message.chat.id,'Верно! Карта, которую я загадал '+ card_number + '-' + card_suit)
    else:
        bot.send_message(message.chat.id, 'Не повезло! Эта карта была ' + card_number + '-' + card_suit)

def hard_compare_diff(message):
    card_number, card_suit = generate_random_card()
    random_card =f'{card_number}+"-"+{card_suit}'
    if message.text == random_card:
        bot.send_message(message.chat.id,'Верно! Карта, которую я загадал '+ card_number + '-' + card_suit)
    else:
        bot.send_message(message.chat.id, 'Не повезло! Эта карта была ' + card_number + '-' + card_suit)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '''Добро пожаловать в игру! 
Я загадаю случайную карту,
попробуй угадай её.''')
   
    keyboard=telebot.types.ReplyKeyboardMarkup()
    easy_button=telebot.types.KeyboardButton('1. Это будет легко')
    mid_button=telebot.types.KeyboardButton('2. Уже поинтересней')
    hard_button=telebot.types.KeyboardButton('3. У тебя нет шансов победить в этой игре')
    
    keyboard.row(easy_button)
    keyboard.row(mid_button)
    keyboard.row(hard_button)

    bot.send_message(message.chat.id,'Выбери сложность игры.', reply_markup=keyboard)
    bot.register_next_step_handler(message, choice_diff)

def choice_diff(message):
    if message.text == '1. Это будет легко':
        keyboard=telebot.types.ReplyKeyboardMarkup()
        red_button=telebot.types.KeyboardButton("🟥")
        black_button=telebot.types.KeyboardButton("⬛️")

        keyboard.row(red_button)
        keyboard.row(black_button)
        
        bot.send_message(message.chat.id, 'Какого цвета загаданная мной карта: 🟥 или ⬛️', reply_markup=keyboard)
        bot.register_next_step_handler(message, easy_compare_message)
 
    elif message.text == '2. Уже поинтересней':
        keyboard = telebot.types.ReplyKeyboardMarkup()
        hearts_button = telebot.types.KeyboardButton('Черви')
        spades_button = telebot.types.KeyboardButton('Пики')
        diamonds_button = telebot.types.KeyboardButton('Бубны')
        clubs_button = telebot.types.KeyboardButton('Трефы')

        keyboard.row(hearts_button)
        keyboard.row(spades_button)
        keyboard.row(diamonds_button)
        keyboard.row(clubs_button)

        bot.send_message(message.chat.id, 'Какой масти я загадал карту ?', reply_markup=keyboard)
        bot.register_next_step_handler(message, mid_compare_message)
   
    else:
        keyboard = telebot.types.ReplyKeyboardMarkup()
        button_h6=telebot.types.KeyboardButton('6-Черви')
        button_h7=telebot.types.KeyboardButton('7-Черви')
        button_h8=telebot.types.KeyboardButton('8-Черви')
        button_h9=telebot.types.KeyboardButton('9-Черви')
        button_h10=telebot.types.KeyboardButton('10-Черви')
        button_hj=telebot.types.KeyboardButton('Валет-Черви')
        button_hq=telebot.types.KeyboardButton('Дама-Черви')
        button_hk=telebot.types.KeyboardButton('Король-Черви')
        button_ha=telebot.types.KeyboardButton('Туз-Черви')
        
        button_s6=telebot.types.KeyboardButton('6-Пики')     
        button_s7=telebot.types.KeyboardButton('7-Пики')     
        button_s8=telebot.types.KeyboardButton('8-Пики')            
        button_s9=telebot.types.KeyboardButton('9-Пики')             
        button_s10=telebot.types.KeyboardButton('10-Пики')           
        button_sj=telebot.types.KeyboardButton('Валет-Пики')         
        button_sq=telebot.types.KeyboardButton('Дама-Пики')          
        button_sk=telebot.types.KeyboardButton('Король-Пики')        
        button_sa=telebot.types.KeyboardButton('Туз-Пики')           
        
        button_d6=telebot.types.KeyboardButton('6-Бубны')
        button_d7=telebot.types.KeyboardButton('7-Бубны')     
        button_d8=telebot.types.KeyboardButton('8-Бубны')            
        button_d9=telebot.types.KeyboardButton('9-Бубны')             
        button_d10=telebot.types.KeyboardButton('10-Бубны')           
        button_dj=telebot.types.KeyboardButton('Валет-Бубны')         
        button_dq=telebot.types.KeyboardButton('Дама-Бубны')          
        button_dk=telebot.types.KeyboardButton('Король-Бубны')        
        button_da=telebot.types.KeyboardButton('Туз-Бубны') 

        button_c6=telebot.types.KeyboardButton('6-Трефы')
        button_c7=telebot.types.KeyboardButton('7-Трефы')     
        button_c8=telebot.types.KeyboardButton('8-Трефы')            
        button_c9=telebot.types.KeyboardButton('9-Трефы')             
        button_c10=telebot.types.KeyboardButton('10-Трефы')           
        button_cj=telebot.types.KeyboardButton('Валет-Трефы')         
        button_cq=telebot.types.KeyboardButton('Дама-Трефы')          
        button_ck=telebot.types.KeyboardButton('Король-Трефы')        
        button_ca=telebot.types.KeyboardButton('Туз-Трефы') 

        keyboard.row(button_h6)
        keyboard.row(button_h7)
        keyboard.row(button_h8)
        keyboard.row(button_h9)
        keyboard.row(button_h10)
        keyboard.row(button_hj)
        keyboard.row(button_hq)
        keyboard.row(button_hk)
        keyboard.row(button_ha)
        
        keyboard.row(button_s6)
        keyboard.row(button_s7)
        keyboard.row(button_s8)
        keyboard.row(button_s9)
        keyboard.row(button_s10)
        keyboard.row(button_sj)
        keyboard.row(button_sq)
        keyboard.row(button_sk)
        keyboard.row(button_sa)
        
        keyboard.row(button_d6)
        keyboard.row(button_d7)
        keyboard.row(button_d8)
        keyboard.row(button_d9)
        keyboard.row(button_d10)
        keyboard.row(button_dj)
        keyboard.row(button_dq)
        keyboard.row(button_dk)
        keyboard.row(button_da)

        keyboard.row(button_c6)
        keyboard.row(button_c7)
        keyboard.row(button_c8)
        keyboard.row(button_c9)
        keyboard.row(button_c10)
        keyboard.row(button_cj)
        keyboard.row(button_cq)
        keyboard.row(button_ck)
        keyboard.row(button_ca)

        bot.send_message(message.chat.id, 'Какую я загадал карту ?', reply_markup=keyboard)
        bot.register_next_step_handler(message,hard_compare_diff)      
        
bot.infinity_polling()




