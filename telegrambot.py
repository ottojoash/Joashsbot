# Run the bot
#bot.polling()
import telebot
import requests
import json

# Replace YOUR_TOKEN with your Telegram bot token
bot = telebot.TeleBot("5819005387:AAFlBtVCLXX4NHI8bMKPsyUhp97wNW4vgB0")

# Replace YOUR_API_KEY and YOUR_CX with your Google Custom Search API key and cx
GOOGLE_CSE_API_KEY = "AIzaSyCdor8vBVac6DBC0E9s_MxjooPNUyE8CWs"
GOOGLE_CSE_CX = "730d22ab9b8f3491f"

@bot.message_handler(commands=['search'])
def search(message):
    # Extract the search query from the message
    search_query = message.text.split(" ", 1)[1]
    # Make a request to the Google Custom Search API
    search_results = requests.get("https://www.googleapis.com/customsearch/v1", params={
        "q": search_query,
        "cx": GOOGLE_CSE_CX,
        "key": GOOGLE_CSE_API_KEY
    })
    # Parse the JSON response
   
