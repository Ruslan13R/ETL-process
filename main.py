# import logging
#
# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
#     filename="logs/etl.log",
#     encoding='utf-8'
# )

from etl.pipeline import Pipeline


if __name__ == '__main__':
    Pipeline().run()
