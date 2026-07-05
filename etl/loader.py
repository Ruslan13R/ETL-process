from etl.connection import Connection


class Loader:
    def load(self, records):
        con = Connection().connect()
        cur = con.cursor()
        query = '''
            INSERT INTO rdl.webm_excel(dt, page_path, query, demand, impressions, position, clicks)
            VALUES(%s, %s, %s, %s, %s, %s, %s)
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

        cur.executemany(query, list_values)

        con.commit()
