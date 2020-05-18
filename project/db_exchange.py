import json
import os

import psycopg2

from logs.log_config import logger

path_to_json_config = 'config.json'

with open(path_to_json_config, 'r') as json_conf_file:
    data = json.loads(json_conf_file.read())
    db = data['postgres']['database']
    host = data['postgres']['host']
    port = data['postgres']['port']
    user = data['postgres']['user']
    password = data['postgres']['password']


def with_connection(func):
    def with_connection_(*args, **kwargs):
        # or use a pool, or a factory function...
        db_conn = psycopg2.connect(database=db,
                                   user=user,
                                   password=password,
                                   host=host,
                                   port=port)
        try:
            rv = func(*args, db_conn, **kwargs)
        except Exception as e:
            db_conn.rollback()
            raise
        else:
            db_conn.commit()  # or maybe not
        finally:
            db_conn.close()

        return rv

    return with_connection_


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
        self.table_name = 'mediafiles'

    @with_connection
    def insert_row(self, new_row_dict, db_conn):
        cur = db_conn.cursor()

        columns = ', '.join(new_row_dict.keys())
        # TODO переделать на изящненько
        values = '\", \"'.join(new_row_dict.values())
        values = values.replace('\'', '\'\'').replace('\"', '\'')

        ins = f"INSERT INTO {self.table_name} ({columns}) VALUES ('{values}')"
        cur.execute(ins)
        logger.info(ins)

    @with_connection
    def get_all_videos(self, db_conn):
        cur = db_conn.cursor()
        # TODO заменить сортировку - по названию
        cur.execute(f'SELECT id, name FROM {self.table_name} ORDER BY id;')

        return {
            'all_videos':
                [dict(zip([column[0] for column in cur.description], row))
                 for row in cur.fetchall()]
        }

    @with_connection
    def get_videos_by_category(self, category_id, db_conn):
        cur = db_conn.cursor()
        cur.execute(f'SELECT id, name FROM {self.table_name} WHERE categories_id = {category_id} ORDER BY id;')

        return {
            'videos_by_category':
                [dict(zip([column[0] for column in cur.description], row))
                 for row in cur.fetchall()]
        }

    @with_connection
    def get_video_info(self, id_db, db_conn):
        # TODO добавить инфу по библиотекам
        cur = db_conn.cursor()
        # TODO заменить сортировку - по названию
        cur.execute(f'SELECT id, categories_id FROM {self.table_name} WHERE id = {id_db};')

        return {
            'video_info':
                [dict(zip([column[0] for column in cur.description], row))
                 for row in cur.fetchall()]
        }

    # SELECT {self.table_name}.id, {self.table_name}.name, {self.table_name}_libs.id
    #     FROM {self.table_name}, {self.table_name}_libs
    #     WHERE city = name;

    @with_connection
    def change_row(self, video_id, changes_dict, db_conn):
        cur = db_conn.cursor()
        changes_str = ', '.join(k + f' = {changes_dict[k]}' for k in changes_dict)
        ins = f'UPDATE {self.table_name} SET {changes_str} WHERE id = {video_id};'
        cur.execute(ins)
        logger.info(ins)

    def delete_videofile(self):
        pass


class CategoriesTable:

    def __init__(self):
        self.table_name = 'categories'

    @with_connection
    def get_all_categories(self, db_conn):
        cur = db_conn.cursor()
        cur.execute(f'SELECT * FROM {self.table_name} ORDER BY id;')

        return {
            'all_categories':
                [dict(zip([column[0] for column in cur.description], row))
                 for row in cur.fetchall()]
        }

    @with_connection
    def add_category(self, name, name_ru, db_conn):
        cur = db_conn.cursor()
        ins = f"INSERT INTO {self.table_name} (name, name_ru) VALUES {name, name_ru} returning id"
        cur.execute(ins)
        db_conn.commit()
        logger.info(ins)

        logger.debug('start FoldersTable from add_category')
        folders = FoldersTable()
        folders.folders_table(cur)

    @with_connection
    def delete_category(self, cat_id, db_conn):
        cur = db_conn.cursor()
        ins = f"DELETE FROM {self.table_name} WHERE id = {cat_id};"
        cur.execute(ins)

        logger.info(ins)


class LibrariesTable:

    def __init__(self):
        self.table_name = 'libraries'

    @with_connection
    def get_all_libraries(self, db_conn):
        cur = db_conn.cursor()
        cur.execute(f'SELECT * FROM {self.table_name} ORDER BY id;')

        return {
            'all_libraries':
                [dict(zip([column[0] for column in cur.description], row))
                 for row in cur.fetchall()]
        }

    @with_connection
    def add_library(self, name, name_ru, db_conn):
        cur = db_conn.cursor()
        ins = f"INSERT INTO {self.table_name} (name, name_ru) VALUES {name, name_ru};"
        cur.execute(ins)
        db_conn.commit()
        logger.info(ins)

        logger.debug('start FoldersTable from add_library')
        db_tbl_folders = FoldersTable()
        db_tbl_folders.folders_table()

    @with_connection
    def delete_library(self, lib_id, db_conn):
        cur = db_conn.cursor()
        ins = f"DELETE FROM {self.table_name} WHERE id = {lib_id};"
        cur.execute(ins)

        logger.info(ins)


class FoldersTable:
    def __init__(self):
        # self.folders_table()
        logger.debug('FoldersTable start')
        self.table_name = 'folders'

    @with_connection
    def folders_table(self, db_conn):
        cur = db_conn.cursor()

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

                    check_row = f'SELECT * FROM {self.table_name} WHERE libraries_id = {lib_id} AND categories_id = {cat_id}'
                    cur.execute(check_row)
                    check_row_answer = cur.fetchall()
                    logger.debug(f'{check_row_answer} for {check_row}')

                    if not check_row_answer:
                        ins = f"INSERT INTO {self.table_name} (libraries_id, categories_id, path) " \
                              f"VALUES ({lib_id}, {cat_id}, '{path}')"
                        cur.execute(ins)
                        logger.info(ins)

    @with_connection
    def get_video_path_folders(self, db_conn):
        cur = db_conn.cursor()

        cur.execute(f'SELECT * FROM {self.table_name} ORDER BY id')
        # results = [r[0] for r in cur.fetchall()]

        return {
            'all_folders':
                [dict(zip([column[0] for column in cur.description], row))
                 for row in cur.fetchall()]
        }


if __name__ == "__main__":
    database = MediaDB()
    # new_row = {
    #     'name': "Dredd.2012.HDRip.XviD.2200MB. rip by [Assassin's Creed]",
    #     # 'categories_id': '1',
    #     'old_path': 'Z:\Plex\Films',
    #     'old_name': "Dredd.2012.HDRip.XviD.2200MB. rip by [Assassin's Creed]",
    #     'sounds': '1'
    # }
    # database.insert_row(new_row)
    print(database.get_all_videos())
    print(database.get_video_info(2))

    # database_libs = LibrariesTable()
    # database_libs.add_library('new_1', 'новая_1')
    # print(database_libs.get_all_libraries())
    # database_libs.delete_library(2)
    # print(database_libs.get_all_libraries())

    # database_cats = CategoriesTable()
    # database_cats.add_category('serials', 'сериалы')
    # print(database_cats.get_all_categories())

    # db_tbl_folders = FoldersTable()
    # db_tbl_folders.folders_table()
    # print(db_tbl_folders.get_video_path_folders())
