import telebot
import time
TOKEN = '6368959206:AAEQ4hz1iH0IvtpwseWmsmLGF588tY2sZRM'  # Замените на токен вашего бота
CHANNEL_ID = '-1002030765344'  # Замените на ID вашего канала

bot = telebot.TeleBot(TOKEN)

def send_message_error_to_channel():
    bot.send_message(CHANNEL_ID, "ГГ кажется бот помер")
def send_message_to_channel(data):
    message = f"""🎮 <b>{data["name"]}</b> 🎮

‼️ <b>{data["team_1"]}</b> - Коэффициент победы: <b>{data["coef_win_1"]}</b>
‼️ <b>{data["team_2"]}</b> - Коэффициент победы: <b>{data["coef_win_2"]}</b>

💰🤑 Поставьте свои ставки сейчас! 🤑💰"""

    bot.send_message(CHANNEL_ID, message, parse_mode="html")
    time.sleep(1)

