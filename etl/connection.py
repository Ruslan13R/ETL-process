import os
import psycopg2
import logging
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

class Connection:
    def connect(self):
        DB_NAME=os.getenv("DB_NAME")
        DB_USER=os.getenv("DB_USER")
        DB_PASSWORD=os.getenv("DB_PASSWORD")
        DB_HOST=os.getenv("DB_HOST")
        DB_PORT=os.getenv("DB_PORT")

        try:
            con = psycopg2.connect(
                dbname=DB_NAME,
                user=DB_USER,
                port=DB_PORT,
                host=DB_HOST,
                password=DB_PASSWORD
            )
            logging.info(f"Connect: {datetime.now()}")
        except Exception as e:
            logging.error(f"Error connect {e}.")
            raise e

        return con
