from etl.extract import Extractor
from etl.transform import Transformer
from etl.loader import Loader


class Pipeline:
    def run(self):
        headers, rows = Extractor().exctract()
        records = Transformer().transform(headers, rows)

        Loader().load(records)

Pipeline().run()