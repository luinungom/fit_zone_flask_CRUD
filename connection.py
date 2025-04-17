from typing import Optional

import mysql
from mysql.connector import Error


class Connection:
    DATABASE = "fit_zone_db"
    USERNAME = "root"
    PASSWORD = "admin"
    DB_PORT = '3306'
    HOST = "localhost"
    POOL_SIZE = 5
    POOL_NAME = 'fit_zone_pool'
    pool = None

    @classmethod
    def get_pool(cls):
        if cls.pool is None:
            try:
                cls.pool = mysql.connector.pooling.MySQLConnectionPool(
                    pool_name=cls.POOL_NAME,
                    pool_size=cls.POOL_SIZE,
                    host=cls.HOST,
                    port=cls.DB_PORT,
                    user=cls.USERNAME,
                    password=cls.PASSWORD,
                    database=cls.DATABASE
                )
                return cls.pool
            except Error as e:
                print(f'Error creating pool: {e}')
        else:
            return cls.pool

    @classmethod
    def get_connection(cls):
        return cls.get_pool().get_connection()

    @classmethod
    def close_connection(cls, connection):
        connection.close()