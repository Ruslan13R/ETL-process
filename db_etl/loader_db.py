import logging
from etl.connection import Connection

class Loader_db:
    def load_db(self, rec):
        try:
            con = Connection().connect()
        except Exception as e:
            logging.error(f"Error to connect. {e}")
            raise e
        else:
            cur = con.cursor()
            query = '''
                INSERT INTO ppl.webmaster_aggregated(dt, query, page_path, demand, impressions, position, clicks) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (dt, page_path, query, impressions, clicks) DO NOTHING;
            '''

        try:
            cur.executemany(query, rec)
            logging.info("Done.")
        except Exception as e:
            logging.error("Error to insert in ppl.webmaster_aggregated")
            raise e
        else:
            con.commit()

        cur.close()
        con.close()
        logging.info("Connect is close.")