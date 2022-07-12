"""A PDF file ingestor."""

import os
import random
from typing import AnyStr, List
import subprocess

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class PDFIngestor(IngestorInterface):
    """A pdf file ingestor.
    
    Ingests pdf files using panda.
    """
    
    allowed_extensions = ['pdf']
    
    @classmethod
    def parse(cls, path: AnyStr) -> List[QuoteModel]:
        """Parse a file.

        Returns: List of QuoteModel
        """
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