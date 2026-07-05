import logging
from openpyxl import load_workbook
from datetime import datetime

class Extractor:
    def exctract(self):
        filename = './data/kirby-msk.xlsx'
        logging.info(f'Start to extract from excel: {datetime.now()}')
        try:
            wd = load_workbook(filename)
        except Exception as e:
            logging.error(f'Error to read: {filename}')
            raise e

        ws = wd.active

        list_of_rows = []

        for row in ws.iter_rows(values_only=True):
            list_of_rows.append(row)

        headers = list_of_rows.pop(0)

        logging.info(f'Lines read and written: {len(list_of_rows)}')

        return headers, list_of_rows
