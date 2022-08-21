import os
import telebot
import pywhatkit as kit
from dotenv import load_dotenv

load_dotenv()

api_token = os.getenv("API_TOKEN")
bot = telebot.TeleBot(api_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
  username = message.from_user.username
  
  bot.reply_to(message, f'Hi {username} Jumpa lagi. Ketik /new untuk langsung memulai atau /help untuk melihat petunjuk yaa 😉.')

@bot.message_handler(commands=['help'])
def send_welcome(message):
  bot.reply_to(message, 'Silahkan tuliskan teks yang akan di convert dengan cara /new <spasi> teks yang ingin diconvert. Contoh: /new Halo saya dari Indonesia.')

@bot.message_handler(commands=['new'])
def send_welcome(message):
  split_teks = message.text.split(' ')[1:]
  teks = ' '.join(split_teks) 
  chat_id = message.chat.id
  username = message.from_user.username
  file_name = f'result{username}{message.date}'
  bot.reply_to(message, 'Sedang Dalam Proses')
  
  kit.text_to_handwriting(teks, save_to=f'{file_name}.png', rgb=(0,0,0))
  bot.send_photo(chat_id, open(f'{file_name}.png', 'rb'))
  bot.reply_to(message, 'Selesai! Silahkan Didownload 😉')

print('Bot is running ... ')
bot.polling()
  