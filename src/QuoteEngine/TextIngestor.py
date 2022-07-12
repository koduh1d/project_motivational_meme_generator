from typing import AnyStr, List

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class TextIngestor(IngestorInterface):
    allowed_extensions = ['txt']
    
    @classmethod
    def parse(cls, path: AnyStr) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        
        models = []
        
        with open(path, 'r') as f:
            for line in f.readlines():
                if len(line) > 0:
                    line = line.strip('\n\r').split(' - ')
                    new_model = QuoteModel(line[0].strip('\"'), line[1])
                    models.append(new_model)
                
        return models