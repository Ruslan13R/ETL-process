from extract import Extractor
from transform import Transformer
from loader import Loader


class Pipeline:
    def run(self):
        headers, rows = Extractor().exctract()
        records = Transformer().transform(headers, rows)

        Loader().load(records)
