"""An object for storing quotes."""

from typing import AnyStr


class QuoteModel:
    """A quote object."""

    def __init__(self, body: AnyStr, author: AnyStr) -> None:
        """Take a body and author string."""
        self.body = body
        self.author = author

    def __repr__(self) -> str:
        """Return: Quote in meme format."""
        return '"' + self.body + '" - ' + self.author
