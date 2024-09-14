# PagePal: Book Recommendation Bot on Telegram
Greetings from PagePal, a Telegram bot that suggests books according to the user-provided genre. PagePal uses the Google Books API to retrieve book information, including the title, author, description, publishing year, and more.

## Features:
- Book recommendations based on genre.
- Details of the book, including the title, author, synopsis, publishing year, language, and a link to a preview.
- Effortlessly user-friendly for any Telegram client.

## Requirements:
- Python 3.7 or above
- Google Books API Key
- Token for Telegram Bot

## Setup

1. Clone the repository
```git clone https://github.com/flykrth/amFOSS-tasks/Task-04/PagePal_bot.git```

Then, move to working directory:
```cd PagePal_bot```

2. Install the dependencies
```pip install python-telegram-bot google-api-python-client```

3. Obtain the API keys
   i) Google Books API key
  ii) Telegram bot token

4. Create an .env file to upload the above credentials (or you can choose to change the variables "GOOGLE_BOOKS_API_KEY" and "TELEGRAM_BOT_TOKEN" locally within the PagePal_bot.py file.

5. Run the bot:
```python3 PagePal_bot.py```

6. Start using your Telegram bot on the app by searching for for the username you gave during the Bot Token generation.
