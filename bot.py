import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Set up the bot and get the update queue
updater = Updater("5819005387:AAFlBtVCLXX4NHI8bMKPsyUhp97wNW4vgB0", use_context=True)
dispatcher = updater.dispatcher

# Define the start command handler
def start(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I am a bot. How can I help you today?")

start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)

# Define the echo command handler
def echo(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

# Start the bot
updater.start_polling()
