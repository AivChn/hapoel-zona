import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram import Bot


BOT_TOKEN = '6564444044:AAGeORejzkiaItlyTT5Uq3H0dAccIwk4jUA'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text: str = update.message.text

    if 'הפועל' == text:
        await update.message.reply_text('זונה')
    elif 'הפועל זונה' == text:
        print('yes')
        await context.bot.pinChatMessage(update.message.chat.id, update.message.message_id)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update: {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting...')
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=1)
