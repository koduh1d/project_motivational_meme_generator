import os
import random
from typing import AnyStr, List
import subprocess

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']
    
    @classmethod
    def parse(cls, path: AnyStr) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        
        models = []
        
        tmp = f'./{random.randint(0,1000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])
        
        with open(tmp, 'r') as f:
            models = []
            lines = [line.strip('\"\r\n').split(' \"') for line in f.readlines() if line.strip()]
            for line in lines:
                for l in line:
                    l = l.split('\" - ')
                    new_model = QuoteModel(l[0], l[1])
                    models.append(new_model)
        os.remove(tmp)

        return models