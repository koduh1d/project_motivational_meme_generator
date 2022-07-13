"""App class."""

import random
import os
from flask import Flask, after_this_request, render_template, abort, request
from MemeGenerator import MemeEngine
from QuoteEngine import Ingestor
from PIL import Image

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for path in quote_files:
        for quote in Ingestor.parse(path):
            quotes.append(quote)

    images_path = "./_data/photos/dog/"

    imgs = [images_path + path for path in os.listdir(images_path)]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    image_url = request.form.get('image_url')
    quote_body = request.form.get('body')
    quote_author = request.form.get('author')
    path = meme.make_meme(image_url, quote_body, quote_author)
    img = Image.open(path)
    tmp = f'./static/{random.randint(0,100000)}.png'
    img = img.save(tmp)
    os.remove(path)
    return render_template('meme.html', path=tmp)

if __name__ == "__main__":
    app.run()
