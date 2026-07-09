import logging

logging.basicConfig(
    level=logging.INFO,
    filename="etl.log",
    filemode='w',
    encoding='utf-8'
)

from etl.pipeline import Pipeline


if __name__ == '__main__':
    Pipeline().run()
    Pipeline().run_db()
