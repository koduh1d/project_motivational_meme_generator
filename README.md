# Overview

A meme generator that creates random memes using motivatinal quotes and pictures of cats (or any other quotes and images)

# Instructions

## How to setup

1. `pip install -r requirements.txt` to install required packages

2. `export FLASK_APP=app.py` to export app file

3. `flask run --host 0.0.0.0 --port 3000 --reload` to run flask

## How to use

Click `random` to generate random images using the preset quotes and images stored in `_data`.

Use creator to create your own meme from scratch by feeding an image url, a quote and an author to the given form.


# Description

There are 2 modules, `MemeGenerator` and `QuoteEngine` that processes all necessary logics.

The `MemeGenerator` has one class that consumes an image path, quotes and author to create an image using the Python PILLOW package.

The `QuoteEngine` has multiple ingestor classes which inherits the `IngestorInterface` preventing repetitive coding and ultimately is parsed by a method `Ingestor` class which compares and chooses the appropriate ingestor depending on the consumed file extension.