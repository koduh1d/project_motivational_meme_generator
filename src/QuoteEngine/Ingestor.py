from typing import AnyStr, List
from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .QuoteModel import QuoteModel
from .TextIngestor import TextIngestor


class Ingestor:
    @staticmethod
    def parse(path: AnyStr) -> List[QuoteModel]:
        ext = path.split('.')[-1]
        if ext == 'pdf':
            return PDFIngestor.parse(path)
        if ext == 'csv':
            return CSVIngestor.parse(path)
        if ext == 'txt':
            return TextIngestor.parse(path)
        if ext == 'docx':
            return DocxIngestor.parse(path)