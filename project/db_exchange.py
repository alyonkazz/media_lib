import json
import os

import psycopg2

from logs.log_config import logger

path_to_json_config = 'config.json'

with open(path_to_json_config, 'r') as f:
    data = json.loads(f.read())
    host = data['postgres']['host']
    port = data['postgres']['port']
    user = data['postgres']['user']
    password = data['postgres']['password']
    database = data['postgres']['database']


# def psycopg2_connect():
#     return psycopg2.connect(database=database,
#                             user=user,
#                             password=password,
#                             host=host,
#                             port=port)


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

        do_it = f"INSERT INTO mediafiles ({columns}) VALUES ('{values}')"
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
        cur.execute(f'SELECT categories_path FROM {self.table_categories} ORDER BY id')
        results = [r[0] for r in cur.fetchall()]
        return results

    def get_all_videos(self):
        db_conn = self.psycopg2_connect()

        cur = db_conn.cursor()
        # TODO заменить сортировку - по названию
        cur.execute(f'SELECT id, name FROM mediafiles ORDER BY id;')
        # results = {r[0]: r[1] for r in cur.fetchall()}
        return {
            'all_videos':
                [dict(zip([column[0] for column in cur.description], row))
                 for row in cur.fetchall()]
        }

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


class CategoriesTable:
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
        cur.execute(f'SELECT * FROM {self.table_name} ORDER BY id;')
        return {
            'all_categories':
                [dict(zip([column[0] for column in cur.description], row))
                 for row in cur.fetchall()]
        }

    def add_category(self, name, name_ru):
        db_conn = self.psycopg2_connect()

        cur = db_conn.cursor()
        ins = f"INSERT INTO {self.table_name} (name, name_ru) VALUES {name, name_ru} returning id"
        cur.execute(ins)
        db_conn.commit()

        folders_table(cur)

        db_conn.commit()
        db_conn.close()

    def delete_category(self, lib_id):
        db_conn = self.psycopg2_connect()

        cur = db_conn.cursor()
        cur.execute(f"DELETE FROM {self.table_name} WHERE id = {lib_id};")
        db_conn.commit()
        db_conn.close()


class LibrariesTable:
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
        cur.execute(f'SELECT * FROM {self.table_name} ORDER BY id;')

        return {
            'all_libraries':
                [dict(zip([column[0] for column in cur.description], row))
                 for row in cur.fetchall()]
        }

    def add_library(self, name, name_ru):
        db_conn = self.psycopg2_connect()

        cur = db_conn.cursor()
        cur.execute(f"INSERT INTO {self.table_name} (name, name_ru) VALUES {name, name_ru};")
        db_conn.commit()

        folders_table(cur)

        db_conn.commit()
        db_conn.close()

    def delete_library(self, lib_id):
        db_conn = self.psycopg2_connect()

        cur = db_conn.cursor()
        cur.execute(f"DELETE FROM {self.table_name} WHERE id = {lib_id};")
        db_conn.commit()
        db_conn.close()


def folders_table(cur):
    database_libs = LibrariesTable()
    database_cats = CategoriesTable()

    all_libraries = database_libs.get_all_libraries()
    all_categories = database_cats.get_all_categories()

    if all_libraries['all_libraries'] and all_categories['all_categories']:
        for i_lib in range(len(all_libraries['all_libraries'])):
            for i_cat in range(len(all_categories['all_categories'])):
                lib_id = all_libraries['all_libraries'][i_lib]['id']
                cat_id = all_categories['all_categories'][i_cat]['id']
                path = f"Z:\\Plex\\" \
                       f"{all_libraries['all_libraries'][i_lib]['name']}" \
                       f"_{all_categories['all_categories'][i_cat]['name']}"

                check_row = f'SELECT * FROM folders WHERE libraries_id = {lib_id} AND categories_id = {cat_id}'
                cur.execute(check_row)
                check_row_answer = cur.fetchall()
                logger.debug(f'{check_row_answer} for {check_row}')

                if not check_row_answer:
                    ins = f"INSERT INTO folders (libraries_id, categories_id, path) " \
                          f"VALUES ({lib_id}, {cat_id}, '{path}')"
                    cur.execute(ins)
                    logger.info(ins)
                    os.mkdir(path)


if __name__ == "__main__":
    database = MediaDB()
    # new_row = {
    #     'name': "Dredd.2012.HDRip.XviD.2200MB. rip by [Assassin's Creed]",
    #     'categories_id': '1'
    # }
    # database.insert_row(new_row)
    # print(database.get_all_videos())
    # print(database.get_video_info(1816))

    # database_libs = LibrariesTable()
    # database_libs.add_library('new_4', 'новая_4')
    # print(database_libs.get_all_libraries())
    # database_libs.delete_library(2)
    # print(database_libs.get_all_libraries())

    # database_cats = CategoriesTable()
    # database_cats.add_category('serials', 'сериалы')
    # print(database_cats.get_all_categories())

    # folders_table('cur')
