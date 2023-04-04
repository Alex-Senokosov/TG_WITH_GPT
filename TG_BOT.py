# openai.api_key = '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'
# TOKEN = '6260578840:AAF8IvgYmk2fMYBt3wHBC3Zzg_0v-XLiSKg'
import telegram
import openai
from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext.filters import MessageFilter

# Установить токен для работы с Telegram API
TOKEN = '6260578840:AAF8IvgYmk2fMYBt3wHBC3Zzg_0v-XLiSKg'
bot = telegram.Bot(token=TOKEN)

# Установить ключ API для работы с CHAT GPT
openai.api_key = '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'

class TextFilter(MessageFilter):
    def filter(self, message):
        return message.text is not None and not message.text.startswith('/')

def generate_response(text):
    # Настроить параметры запроса
    prompt = f"Q: {text}\nA:"

    # Создать запрос к CHAT GPT
    response = openai.Completion.create(
        engine='davinci',
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )

    # Получить сгенерированный ответ от CHAT GPT
    answer = response.choices[0].text.strip()

    return answer

def handle_message(update, context):
    # Получить текст сообщения от пользователя
    user_text = update.message.text

    # Сгенерировать ответ на основе запроса пользователя
    bot_response = generate_response(user_text)

    # Отправить ответ пользователю
    update.message.reply_text(bot_response)

def main():
    # Создать экземпляр класса Updater и добавить обработчики

    dispatcher = updater.dispatcher
    message_handler = MessageHandler(TextFilter())
    dispatcher.add_handler(message_handler)

    # Запустить бота
    start_polling()

    # Остановить бота при нажатии Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
