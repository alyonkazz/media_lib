import psycopg2


class SingletonMeta(type):
    def __init__(cls, *args, **kwargs):
        cls._instance = None
        # глобальная точка доступа `Singleton.get_instance()`
        cls.get_instance = classmethod(lambda c: c._instance)
        super(SingletonMeta, cls).__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instance


class MediaDB(metaclass=SingletonMeta):
    def __init__(self):
        self.host = '192.168.2.8'
        self.port = '5432'
        self.user = "postgres"
        self.password = ''
        self.database = 'filmLib'
        self.table_name = 'film_lib'

    def psycopg2_connect(self):
        return psycopg2.connect(database=self.database,
                                   user=self.user,
                                   password=self.password,
                                   host=self.host,
                                   port=self.port)

    def insert_row(self, new_row_dict):
        db_conn = self.psycopg2_connect()

        cur = db_conn.cursor()
        columns = ', '.join(tuple(new_row_dict.keys()))
        values = tuple(new_row_dict.values())
        do_it = f"INSERT INTO {self.table_name} ({columns}) VALUES {values};"
        cur.execute(do_it)
        db_conn.commit()
        db_conn.close()

    def get_column(self, column):
        db_conn = self.psycopg2_connect()

        cur = db_conn.cursor()
        # TODO заменить сортировку - по названию
        cur.executemany(f'SELECT {column} FROM {self.table_name} ORDER BY id')
        results = [r[0] for r in cur.fetchall()]
        return results

    def get_videos(self):
        db_conn = self.psycopg2_connect()

        cur = db_conn.cursor()
        # TODO заменить сортировку - по названию
        cur.execute(f'SELECT id, name FROM {self.table_name} ORDER BY id')
        results = {r[0]: r[1] for r in cur.fetchall()}
        return results

    def get_videos_by_category(self, category_id):
        db_conn = self.psycopg2_connect()

        cur = db_conn.cursor()
        cur.execute(f'SELECT id, name FROM {self.table_name} WHERE categories_id = {category_id} ORDER BY id')
        results = {r[0]: r[1] for r in cur.fetchall()}
        return results

    def get_video_info(self, id_db):
        db_conn = self.psycopg2_connect()

        cur = db_conn.cursor()
        # TODO заменить сортировку - по названию
        cur.execute(f'SELECT id, our_lib, moms_lib, categories_id FROM {self.table_name} WHERE id = {id_db}')
        results = cur.fetchall()[0]
        return results

    def change_row(self, id_db, **kwargs):
        db_conn = self.psycopg2_connect()

        cur = db_conn.cursor()
        for k, v in kwargs.items():
            cur.execute(f"UPDATE {self.table_name} SET {k} = '{v}' WHERE id = {id_db};")
        db_conn.commit()
        db_conn.close()


if __name__ == "__main__":
    database = MediaDB()
    new_row = {
        'name': 'Aristocats.1970.BDRip-AVC.Rus.Ukr.Eng.mkv',
        'categories_id': '1'
    }

    # columns = ', '.join(map(str, tuple(new_row_dict.keys())))
    # values = ', '.join(tuple(new_row_dict.values()))
    # print(f"-- INSERT INTO fghfgh ({columns}) VALUES ({values});")
    # print(columns)
    # print(list(new_row_dict.keys())[0])

    database.insert_row(new_row)
    # database.change_row('1846', name='ljlh111h', our_lib='false', categories_id='2')
    # print(get_column('*')[13])
    # print(database.get_videos())
    # print(database.get_video_info(1816))
