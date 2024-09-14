# The below script has only framework code and contain bugs. Therefore, this project is not finished.

import os
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv

load_dotenv()
GOOGLE_BOOKS_API_KEY = os.getenv('GOOGLE_BOOKS_API_KEY')

# Function to fetch books using Google Books API
def get_books_by_genre(genre):
    url = f"https://www.googleapis.com/books/v1/volumes?q=subject:{genre}&key={GOOGLE_BOOKS_API_KEY}"
    response = requests.get(url)
    books = response.json().get('items', [])
    
    book_list = []
  
    for book in books:
        info = book['volumeInfo']
        book_list.append({
            'title': info.get('title', 'No Title Available'),
            'authors': ', '.join(info.get('authors', 'Unknown Author')),
            'description': info.get('description', 'No description available.'),
            'year': info.get('publishedDate', 'N/A'),
            'language': info.get('language', 'N/A'),
            'previewLink': info.get('previewLink', 'N/A')
        })
    return book_list

async def start(update: Update, context) -> None:
    await update.message.reply_text(
        "Hello! I am PagePal, your personal book recommendation bot. "
        "Type a genre (like 'Fantasy' or 'Science Fiction') and I'll find some great books for you!"
    )

# Bot handler for genre recommendations
async def recommend_books(update: Update, context) -> None:
    genre = update.message.text
    books = get_books_by_genre(genre)
    
    if books:
        for book in books[:5]:  # Displays only upto top 5 results
            message = (
                f"*{book['title']}*\n"
                f"Author: {book['authors']}\n"
                f"Year: {book['year']}\n"
                f"Description: {book['description']}\n"
                f"[Preview Link]({book['previewLink']})\n"
            )
            await update.message.reply_text(message, parse_mode='Markdown')
    else:
        await update.message.reply_text("Sorry, I couldn't find any books for that genre.")

# Main function
async def main():
    # Initialization
    application = Application.builder().token(os.getenv('TELEGRAM_BOT_TOKEN')).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, recommend_books))
  
    await application.initialize()
    await application.start()
    await application.idle()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
