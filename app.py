import telebot
import time
TOKEN = '6368959206:AAEQ4hz1iH0IvtpwseWmsmLGF588tY2sZRM'  # Замените на токен вашего бота
CHANNEL_ID = "-1002001164153"
CHANNEL_ID = '-1002030765344'  # Замените на ID вашего канала

bot = telebot.TeleBot(TOKEN)

def send_message_error_to_channel(url):
    bot.send_message(CHANNEL_ID, f"ГГ кажется бот помер\n {url}")

def send_massage_new_parsing(url):
    bot.send_message(CHANNEL_ID, f"Новая страница парсится {url}")
def send_message_to_channel(data):
    if data["coef_draw"]!=0:
        message = f"""🧨 { 'Counter-Strike' if data["is_cs"] else 'Dota'} 🧨
🎮 {data["name"]} 🎮

‼️ <b>{data["team_1"]}</b> - Коэффициент победы: <b>{data["coef_win_1"]}</b>
‼️ <b>{data["draw"]}</b> - Коэффициент победы: <b>{data["coef_draw"]}</b>
‼️ <b>{data["team_2"]}</b> - Коэффициент победы: <b>{data["coef_win_2"]}</b>

⏱ {data["datee"]} {data["timee"]} ⏱

💰🤑 Поставьте свои ставки сейчас! 🤑💰"""
    else:
        message = f"""🧨 { 'Counter-Strike' if data["is_cs"] else 'Dota'} 🧨
🎮 {data["name"]} 🎮

‼️ <b>{data["team_1"]}</b> - Коэффициент победы: <b>{data["coef_win_1"]}</b>
‼️ <b>{data["team_2"]}</b> - Коэффициент победы: <b>{data["coef_win_2"]}</b>

⏱ {data["datee"]} {data["timee"]} ⏱

💰🤑 Поставьте свои ставки сейчас! 🤑💰"""
    time.sleep(3)
    bot.send_message(CHANNEL_ID, message, parse_mode="html")
    
