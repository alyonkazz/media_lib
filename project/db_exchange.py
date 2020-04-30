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
        self.table_categories = 'categories'

    def psycopg2_connect(self):
        return psycopg2.connect(database=self.database,
                                   user=self.user,
                                   password=self.password,
                                   host=self.host,
                                   port=self.port)

    def insert_row(self, new_row_dict):
        db_conn = self.psycopg2_connect()

        cur = db_conn.cursor()
        columns = ', '.join(new_row_dict.keys())
        # TODO переделать на изящненько
        values = '\", \"'.join(new_row_dict.values())
        values = values.replace('\'', '\'\'').replace('\"', '\'')

        do_it = f"INSERT INTO {self.table_name} ({columns}) VALUES ('{values}');"
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

    def get_video_path_folders(self):
        db_conn = self.psycopg2_connect()

        cur = db_conn.cursor()
        cur.execute(f'SELECT categories_path FROM {self.table_categories} ORDER BY id')
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

    def change_row(self, video_id, changes_dict):
        db_conn = self.psycopg2_connect()

        cur = db_conn.cursor()
        changes_str = ', '.join(k + f' = {changes_dict[k]}' for k in changes_dict)
        cur.execute(f'UPDATE {self.table_name} SET {changes_str} WHERE id = {video_id};')
        db_conn.commit()
        db_conn.close()


if __name__ == "__main__":
    database = MediaDB()
    new_row = {
        'name': "Dredd.2012.HDRip.XviD.2200MB. rip by [Assassin's Creed]",
        'categories_id': '1'
    }

    database.insert_row(new_row)

    # changes_dict = {
    #     # "name": "5555",
    #     "our_lib": "false",
    #     "moms_lib": "false",
    #     "categories_id": "2"
    # }
    # print(changes_dict)
    # database.change_row('1858', changes_dict)
    # database.change_row('1859', name='222222222', our_lib='false', categories_id='2')

    # database.change_row('1846', {name = 'ljlh111h', our_lib = 'false', categories_id = '2'})

    # print(get_column('*')[13])
    # print(database.get_videos())
    # print(database.get_video_info(1816))
