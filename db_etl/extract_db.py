import logging
import psycopg2
from datetime import datetime
from etl.connection import Connection


class Extractor_db:
    def extract_db(self):
        # Подключаемся к БД
        try:
            con = Connection().connect()
            logging.info(f'Connect in extract from extract_rdl: {datetime.now()}')
        except Exception as e:
            raise e

        # Формируем запрос
        cur = con.cursor()
        query = '''
            SELECT 
                dt,
                query,
                page_path,
                demand,
                impressions,
                position,
                clicks    
            FROM rdl.webm_excel
        '''
        # Получаем строки
        cur.execute(query)
        res = cur.fetchall()

        cur.close()
        con.close()

        return res
