import telebot

API_TOKEN = "7590969005:AAGywh2HslfIHgDPAiHQVdAB-0HnwqRIB3A"
GROUP_CHAT_ID = -1002150637572  # ID твоей группы

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(message.chat.id,
        "👋 Добро пожаловать в 1-Apllya\n"
        "✍️ Введи номер телефона, который хочешь сдать:"
    )

@bot.message_handler(func=lambda message: True)
def handle_number(message):
    user = f"@{message.from_user.username}" if message.from_user.username else "Без username"
    number = message.text.strip()

    # Отправка в группу
    bot.send_message(GROUP_CHAT_ID,
        f"📥 Новый номер сдан: {number}\n👤 От: {user}"
    )

    # Ответ пользователю
    bot.send_message(message.chat.id,
        "✅ Спасибо, номер принят.\n💰 Отчёты и выплата будут ночью или утром."
    )

bot.polling()