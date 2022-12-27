import telegram
from telegram.ext import Updater, MessageHandler, Filters

# Set up the bot and get the update queue
updater = Updater("5819005387:AAFlBtVCLXX4NHI8bMKPsyUhp97wNW4vgB0", use_context=True)
dispatcher = updater.dispatcher

# Define the message handler function
def message_handler(update, context):
  # Get the incoming message
  message = update.message
  text = message.text

  # Check the incoming message and respond accordingly
  if "hello" in text.lower():
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, how are you today?")
  elif "goodbye" in text.lower():
    context.bot.send_message(chat_id=update.effective_chat.id, text="Goodbye, have a nice day!")
  else:
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm sorry, I didn't understand your message.")

# Set up the message handler
message_handler = MessageHandler(Filters.text, message_handler)
dispatcher.add_handler(message_handler)

# Start the bot
updater.start_polling()
