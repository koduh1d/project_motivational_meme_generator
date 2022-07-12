from typing import AnyStr, List
import docx

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class DocxIngestor(IngestorInterface):
    allowed_extensions = ['docx']
    
    @classmethod
    def parse(cls, path: AnyStr) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        
        models = []
        
        doc = docx.Document(path)
        for line in doc.paragraphs:
            if len(line.text) > 0:
                line = line.text.strip('\n\r').split(' - ')
                new_model = QuoteModel(line[0].strip('\"'), line[1])
                models.append(new_model)

        return models