import json

import psycopg2

path_to_json_config = 'config.json'

with open(path_to_json_config, 'r') as f:
    data = json.loads(f.read())
    host = data['postgres']['host']
    port = data['postgres']['port']
    user = data['postgres']['user']
    password = data['postgres']['password']
    database = data['postgres']['database']


def psycopg2_connect():
    return psycopg2.connect(database=database,
                            user=user,
                            password=password,
                            host=host,
                            port=port)


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
        with open(path_to_json_config, 'r') as f:
            data = json.loads(f.read())
            self.host = data['postgres']['host']
            self.port = data['postgres']['port']
            self.user = data['postgres']['user']
            self.password = data['postgres']['password']
            self.database = data['postgres']['database']

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

        do_it = f"INSERT INTO mediafiles ({columns}) VALUES ('{values}');"
        cur.execute(do_it)
        db_conn.commit()
        db_conn.close()

    # def get_column(self, column):
    #     db_conn = self.psycopg2_connect()
    #
    #     cur = db_conn.cursor()
    #     # TODO заменить сортировку - по названию
    #     cur.executemany(f'SELECT {column} FROM mediafiles ORDER BY id')
    #     results = [r[0] for r in cur.fetchall()]
    #     return results

    def get_video_path_folders(self):
        db_conn = self.psycopg2_connect()

        cur = db_conn.cursor()
        cur.execute(f'SELECT categories_path FROM {self.table_categories} ORDER BY id;')
        results = [r[0] for r in cur.fetchall()]
        return results

    def get_videos(self):
        db_conn = self.psycopg2_connect()

        cur = db_conn.cursor()
        # TODO заменить сортировку - по названию
        cur.execute(f'SELECT id, name FROM mediafiles ORDER BY id;')
        results = {r[0]: r[1] for r in cur.fetchall()}
        return results

    def get_videos_by_category(self, category_id):
        db_conn = self.psycopg2_connect()

        cur = db_conn.cursor()
        cur.execute(f'SELECT id, name FROM mediafiles WHERE categories_id = {category_id} ORDER BY id;')
        results = {r[0]: r[1] for r in cur.fetchall()}
        return results

    def get_video_info(self, id_db):
        # TODO добавить инфу по библиотекам
        db_conn = self.psycopg2_connect()

        cur = db_conn.cursor()
        # TODO заменить сортировку - по названию
        cur.execute(f'SELECT id, categories_id FROM mediafiles WHERE id = {id_db};')
        results = cur.fetchall()[0]
        return results

    # SELECT mediafiles.id, mediafiles.name, mediafiles_libs.id
    #     FROM mediafiles, mediafiles_libs
    #     WHERE city = name;

    def change_row(self, video_id, changes_dict):
        db_conn = self.psycopg2_connect()

        cur = db_conn.cursor()
        changes_str = ', '.join(k + f' = {changes_dict[k]}' for k in changes_dict)
        cur.execute(f'UPDATE mediafiles SET {changes_str} WHERE id = {video_id};')
        db_conn.commit()
        db_conn.close()

    def delete_videofile(self):
        pass


class CategoriesDB:
    table_name = 'categories'

    def __init__(self):
        with open(path_to_json_config, 'r') as f:
            data = json.loads(f.read())
            self.host = data['postgres']['host']
            self.port = data['postgres']['port']
            self.user = data['postgres']['user']
            self.password = data['postgres']['password']
            self.database = data['postgres']['database']

    def psycopg2_connect(self):
        return psycopg2.connect(database=self.database,
                                user=self.user,
                                password=self.password,
                                host=self.host,
                                port=self.port)

    def get_all_categories(self):
        db_conn = self.psycopg2_connect()

        cur = db_conn.cursor()
        cur.execute(f'SELECT id, name_ru FROM {self.table_name} ORDER BY id;')
        results = {r[0]: r[1] for r in cur.fetchall()}
        return results

    def add_category(self, name, name_ru):
        db_conn = self.psycopg2_connect()

        cur = db_conn.cursor()
        cur.execute(f"INSERT INTO {self.table_name} (name, name_ru) VALUES {name, name_ru};")
        db_conn.commit()
        db_conn.close()

    def delete_category(self, lib_id):
        db_conn = self.psycopg2_connect()

        cur = db_conn.cursor()
        cur.execute(f"DELETE FROM {self.table_name} WHERE id = {lib_id};")
        db_conn.commit()
        db_conn.close()
        

class LibrariesDB:
    table_name = 'libraries'

    def __init__(self):
        with open(path_to_json_config, 'r') as f:
            data = json.loads(f.read())
            self.host = data['postgres']['host']
            self.port = data['postgres']['port']
            self.user = data['postgres']['user']
            self.password = data['postgres']['password']
            self.database = data['postgres']['database']

    def psycopg2_connect(self):
        return psycopg2.connect(database=self.database,
                                user=self.user,
                                password=self.password,
                                host=self.host,
                                port=self.port)

    def get_all_libraries(self):
        db_conn = self.psycopg2_connect()

        cur = db_conn.cursor()
        cur.execute(f'SELECT id, name_ru FROM {self.table_name} ORDER BY id;')
        results = {r[0]: r[1] for r in cur.fetchall()}
        return results

    def add_library(self, name, name_ru):
        db_conn = self.psycopg2_connect()

        cur = db_conn.cursor()
        cur.execute(f"INSERT INTO {self.table_name} (name, name_ru) VALUES {name, name_ru};")
        db_conn.commit()
        db_conn.close()

    def delete_library(self, lib_id):
        db_conn = self.psycopg2_connect()

        cur = db_conn.cursor()
        cur.execute(f"DELETE FROM {self.table_name} WHERE id = {lib_id};")
        db_conn.commit()
        db_conn.close()


if __name__ == "__main__":
    database = MediaDB()

    # new_row = {
    #     'name': "Dredd.2012.HDRip.XviD.2200MB. rip by [Assassin's Creed]",
    #     'categories_id': '1'
    # }
    # database.insert_row(new_row)

    # changes_dict = {
    #     # "name": "5555",
    #     "our_lib": "false",
    #     "moms_lib": "false",
    #     "categories_id": "2"
    # }
    # print(get_column('*')[13])
    # print(database.get_videos())
    # print(database.get_video_info(1816))

    database_libs = LibrariesDB()
    # database_libs.add_library('serials', 'сериалы')
    # print(database_libs.get_all_libraries())
    database_libs.delete_library(2)
    print(database_libs.get_all_libraries())

    # database_cats = CategoriesDB()
    # print(database_cats.get_all_categories())
