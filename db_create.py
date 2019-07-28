#!/usr/bin/python
import os
import psycopg2
from config import config
from queries import department_sql, employee_sql, tables_sql
from utils import load_json

#env var for json file
JSON = str(os.environ.get('JSON', default="data.json"))


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # add tables to the database
        cur.execute(tables_sql)

        # get data from json
        insert_department_list, insert_employee_list = load_json(JSON)

        # add data to the tables
        print("Inserting data ...")
        cur.execute(department_sql + insert_department_list)
        cur.execute(employee_sql + insert_employee_list)

        #commit changes to the database
        print("Commiting changes ...")
        conn.commit()

        # close the communication with the PostgreSQL
        print("Job is done.")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()