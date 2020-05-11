# -*- coding: utf-8 -*-
import json
import psycopg2
import sys

from logs.log_config import logger
path_to_json_config = 'config.json'


class CheckDB:
    def __init__(self):

        with open(path_to_json_config, 'r') as f:
            data = json.loads(f.read())
            self.host = data['postgres']['host']
            self.port = data['postgres']['port']
            self.user = data['postgres']['user']
            self.password = data['postgres']['password']
            self.database = data['postgres']['database']

        self.table_media_lib = 'media_lib'
        self.table_categories = 'categories'

        self.try_connect_to_db()
        self.try_connect_to_tables()

    def psycopg2_connect(self):
        return psycopg2.connect(database=self.database,
                                user=self.user,
                                password=self.password,
                                host=self.host,
                                port=self.port)

    def try_connect_to_db(self):
        con = None
        try:
            con = self.psycopg2_connect()
            logger.debug(f'connect to database {self.database} success')

        except psycopg2.Error as e:
            logger.critical(e)
            sys.exit(1)

        finally:
            if con:
                con.close()

    def try_connect_to_tables(self):
        table_names = ['mediafiles', 'mediafiles_libs', 'libraries', 'categories', 'folders']
        for table_name in table_names:
            self.check_table(table_name)

    def check_table(self, table_name):
        con = None
        try:
            con = self.psycopg2_connect()
            cur = con.cursor()
            cur.execute(f'SELECT 1 from {table_name}')
            ver = cur.fetchone()
            logger.debug(f'connect to table {table_name} success')

        except psycopg2.Error as e:
            logger.critical(e)

        finally:
            if con:
                con.close()


if __name__ == "__main__":
    CheckDB()
