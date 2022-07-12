from abc import ABC, abstractmethod
from typing import AnyStr, List
from .QuoteModel import QuoteModel

class IngestorInterface(ABC):
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path):
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions
    
    @staticmethod
    @abstractmethod
    def parse(cls, path: AnyStr) -> List[QuoteModel]:
        pass