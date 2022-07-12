"""An interface for Ingestor objects."""

from abc import ABC, abstractmethod
from typing import AnyStr, List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """An abstract class for Ingestor classes."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path):
        """Check for valid file extension."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @staticmethod
    @abstractmethod
    def parse(cls, path: AnyStr) -> List[QuoteModel]:
        """Parse appropriate files.

        Returns: List of QuoteModel objects
        """
        pass
