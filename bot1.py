from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Определяем функцию для обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Напиши мне что-нибудь, и я повторю это.')

# Определяем функцию для обработки текстовых сообщений
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)

# Основная функция для запуска бота
def main() -> None:
    application = ApplicationBuilder().token("7879043605:AAGaaZVomJsaY-RX50ZWRyggeYzg34rwRho").build()

    # Регистрация обработчиков команд и сообщени
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()