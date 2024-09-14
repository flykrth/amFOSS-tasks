# PagePal

## Project overview
PagePal is a Telegram bot that provides book recommendations based on user-specified genres. It retrieves book information from the Google Books API and shows users the title, author, description, year of publication, language, and preview link of each book.

Thus helping people find new books in their preferred categories is the main goal of the bot.

## Features
1. Search for books by genre
2. Retrieve information about the book including title, author, description, year of publication, language and a link to preview the book
3. Accessible and interactive through the Telegram app client.

# Code documentation
The project has a straightforward structure, and the PagePal_bot.py script, which manages the bot's logic and communication with the Google Books API, is its main constituent.

## Main Components:
1. ```get_books_by_genre(genre)```:
The task of retrieving book data from the Google Books API falls to this function. It builds a query and asks the API for up to five books based on the genre that is supplied. Book title, author, description, year, language, and preview link are among the information that is returned.

2. Bot Handlers:
```start(update, context)```: Sends a welcome message when the user starts the bot.
```recommend_books(update, context)```: Responds to user input, fetches the relevant books based on the provided genre, and formats the response for the user.

3. API Integration:
- Google Books API integration allows querying books by genre.
- The PagePal bot is created using the ```python-telegram-bot``` library, which facilitates the interaction between users and the bot.

## Key functions:
1. ```get_books_by_genre(genre)```:
Input: Genre (string)
Output: List of books with details (title, author, description, etc.)
Usage: Called when the user types in a genre. Fetches up to 5 books from the Google Books API and formats the result for display in the Telegram chat.

2. ```start(update, context)```:
Functionality: Sends a welcome message to the user when the bot is started.
Usage: Automatically triggered when a user starts the bot using the /start command.

3. ```recommend_books(update, context)```:
Functionality: Fetches and displays book recommendations based on the user’s input.
Usage: Triggered when the user sends any text message (which is treated as a genre) to the bot.
