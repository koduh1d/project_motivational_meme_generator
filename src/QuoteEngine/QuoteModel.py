from typing import AnyStr

class QuoteModel:
    def __init__(self, body: AnyStr, author: AnyStr) -> None:
        self.body = body
        self.author = author
        
    def __repr__(self) -> str:
        return '"' + self.body + '" - ' + self.author