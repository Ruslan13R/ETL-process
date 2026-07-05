import logging
from datetime import datetime


class Transformer:
    def transform(self, headers, rows):
        logging.info(f"String transform started: {datetime.now()}")
        records = []

        for row in rows:
            query = row[0]
            url = row[1]

            temp_date_of_metrics = {}

            for head in range(2, len(headers)):
                date, metric = headers[head].split('_')

                if date not in temp_date_of_metrics:
                    temp_date_of_metrics[date] = {}

                temp_date_of_metrics[date][metric] = row[head]

            for dt, mt in temp_date_of_metrics.items():
                records.append(
                    {
                       'dt': dt,
                        'query': query,
                        'page_path': url,
                        'shows': mt['shows'],
                        'position': mt['position'],
                        'demand': mt['demand'],
                        'ctr': mt['ctr'],
                        'clicks': mt['clicks']
                    }
                )

        logging.info(f"Number of recycled records: {len(records)}")

        return records
