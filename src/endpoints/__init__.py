import os
import mysql.connector


def mysqlconnector():
    return mysql.connector.connect(
        host=os.environ["MYSQL_HOST"],
        port=os.environ["MYSQL_PORT"],
        database=os.environ["MYSQL_DATABASE"],
        user=os.environ["MYSQL_USER"],
        password=os.environ["MYSQL_PASSWORD"],
    )
