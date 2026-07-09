import logging

class Transformer_db:
    def transform_db(self, records):
        correct_rows = []

        for rec in records:
            dt = rec[0]
            query = rec[1]
            url = rec[2]
            demand = rec[3]
            impressions = rec[4]
            position = rec[5]
            clicks = rec[6]

            if demand < 0 or impressions < 0 or clicks < 0:
                logging.info(f"{query}: Negative values")
                continue

            if clicks > impressions:
                logging.info(f"{query}: clicks > impressions")
                continue

            if clicks > 0 and impressions == 0:
                logging.info(f"{query}: clicks without impressions")
                continue

            correct_rows.append(rec)

        return correct_rows


