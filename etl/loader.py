from etl.connection import Connection
from datetime import datetime
import logging

class Loader:
    def load(self, records):
        logging.info(f"Uploading records to the database (Postgresql): {datetime.now()}")

        try:
            con = Connection().connect()
        except Exception as e:
            logging.error("Error to connect database. During the loading in database.")
            raise e

        cur = con.cursor()
        query = '''
            INSERT INTO rdl.webm_excel(dt, page_path, query, demand, impressions, position, clicks)
            VALUES(%s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (dt, page_path, query, impressions, clicks) DO NOTHING;
        '''

        list_values = []

        for record in records:
            list_values.append(
                (
                    record['dt'],
                    record['page_path'],
                    record['query'],
                    record['demand'],
                    record['shows'],
                    record['position'],
                    record['clicks']
                )
            )

        try:
            logging.info(f"Start to load records: {datetime.now()}")
            cur.executemany(query, list_values)
        except Exception as e:
            logging.error('Error to insert records')
            raise e
        else:
            logging.info(f"Total records: {len(list_values)}")

        con.commit()
        cur.close()
        con.close()
