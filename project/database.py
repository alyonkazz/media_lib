"""

Задача:
 Реализовать как минимум один порождающий паттерн в домашнем приложении.

 Использован паттерн Одиночка

"""

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
        self.password = '200289'
        self.database = 'filmLib'
        self.table_name = 'film_lib'

    def get_column(self, column):
        db_conn = psycopg2.connect(database=self.database,
                                   user=self.user,
                                   password=self.password,
                                   host=self.host,
                                   port=self.port)

        cur = db_conn.cursor()
        # TODO заменить сортировку - по названию
        cur.execute(f'SELECT {column} FROM {self.table_name} ORDER BY id')
        results = cur.fetchall()
        return list(results)

    def change_row(self, id_db, **kwargs):
        db_conn = psycopg2.connect(database=self.database,
                                   user=self.user,
                                   password=self.password,
                                   host=self.host,
                                   port=self.port)

        cur = db_conn.cursor()
        for k, v in kwargs.items():
            cur.execute(f"UPDATE {self.table_name} SET {k} = '{v}' WHERE id = {id_db};")
        db_conn.commit()
        db_conn.close()


if __name__ == "__main__":
    database = MediaDB()
    # database.change_row('1820', name='ljlh111h', our_lib='false')
    # print(get_column('*')[13])
    print(database.get_column('*'))
