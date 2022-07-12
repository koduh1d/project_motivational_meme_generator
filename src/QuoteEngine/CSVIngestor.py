"""A csv file ingestor."""

from typing import AnyStr, List
import pandas
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class CSVIngestor(IngestorInterface):
    """A csv file ingestor.

    Ingests csv files using panda.
    """

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: AnyStr) -> List[QuoteModel]:
        """Parse a file.

        Returns: List of QuoteModel
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        models = []
        df = pandas.read_csv(path, header=0)
        for index, row in df.iterrows():
            new_model = QuoteModel(row['body'], row['author'])
            models.append(new_model)
        return models
