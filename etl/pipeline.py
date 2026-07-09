from etl.extract import Extractor
from etl.transform import Transformer
from etl.loader import Loader
from db_etl.extract_db import Extractor_db
from db_etl.transform_db import Transformer_db
from db_etl.loader_db import Loader_db


class Pipeline:
    def run(self):
        headers, rows = Extractor().exctract()
        records = Transformer().transform(headers, rows)

        Loader().load(records)

    def run_db(self):
        records = Extractor_db().extract_db()
        transform = Transformer_db().transform_db(records)

        Loader_db().load_db(transform)

