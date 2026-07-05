from connection import Connection


class Loader:
    def load(self, records):
        cur = Connection().connect().cursor()
        query = '''
            INSERT INTO rdl.webm_excel(dt, page_path, query, demand, position, clicks)
            VALUES(%s, %s, %s, %s, %s, %s)
        '''

        list_values = []

        for record in records:
            list_values.append(
                (
                    record['dt'],
                    record['page_path'],
                    record['query'],
                    record['demand'],
                    record['position'],
                    record['clicks']
                )
            )

        cur.executemany(query, list_values)
