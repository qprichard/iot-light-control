"""
Class for the database management

if you want to create tables by a script, you have to add script_db
"""

import sqlite3 as lite
import sys
import os

class Database():
    def __init__(self, db_name, db_script=None):
        self.db_name  = db_name
        con = None
        cur = None
        try:
            exist = os.path.isfile(f"./{self.db_name}")
            if  not exist:
                print(f"{self.db_name} file will be created")
                if db_script:
                    print(f"{db_script} will be executed")

            con = lite.connect(self.db_name)
            cur = con.cursor()
            cur.execute('SELECT SQLITE_VERSION()')
            data = cur.fetchone()[0]

            print(f"SQLITE version: {data}")

            con.commit()

            if not exist and db_script:
                self.init_db(db_script)

        except lite.Error as e:
            print(f"Error {e.args[0]}")
            sys.exit(1)

        finally:
            if con:
                con.close()

    def init_db(self, db_script):
        print(f'creating a database with script {db_script}')
        try:
            file = open(db_script, 'r').read()
            con = lite.connect(self.db_name)
            cur = con.cursor()
            cur.executescript(file)
            con.commit()
            print('database created.');
        except lite.Error as e:
            print(f"Error {e.args[0]}")

        finally:
            con.close()

    def insert(self, table, values, params = None, many=False):
        try:
            con = lite.connect(self.db_name)
            cur = con.cursor()

            execute = cur.executemany if many else cur.execute

            #get number of empty values
            empty_values = ['?']*len(values[0]) if many else ['?']*len(values)

            #get form of params
            table_params = con.execute(f"PRAGMA table_info({table})");
            table_params = table_params.fetchall()
            table_params = [ elem[1] for elem in table_params]
            table_params.remove('id')

            has_params = f"({params})" if params else f"({','.join(table_params)})";

            sql = f"INSERT INTO {table} {has_params} VALUES({','.join(empty_values)});"
            execute(sql, values)
            con.commit()
            print(f'tuple inserted: {sql} \n { values}')
        except lite.Error as e:
            if con:
                con.rollback()
            print(f'Error: {e.args[0]}')
        finally:
            con.close()


    def select(self, table=None, conditions=None, params=None, query=None, many=False):
        """
            table = string
            conditions = list of tuples [(param, value, operator="="), (...,...,...)]
            params = tuple
            query = string
        """
        assert table is not None if conditions is not None else True
        assert table is None and conditions is None if query is not None else True


        sql = "";
        if table:
            sql_conditions = None
            if conditions:
                sql_conditions = []
                for condition in conditions:
                    param = condition[0]
                    value = condition[1]
                    try:
                        operator = condition[2]
                    except:
                        operator = "="
                    sql_conditions.append(f"{param}{operator}'{value}'")
                sql_conditions = " and ".join(sql_conditions)

            sql_conditions = f" WHERE {sql_conditions}" if sql_conditions else "";
            sql = f"SELECT {params if params else '*'} FROM {table}{ sql_conditions };"

        if query:
            sql = query;

        try:
            con = lite.connect(self.db_name)
            cur = con.cursor()
            print(sql)
            cur.execute(sql)

            rows = cur.fetchall() if many else cur.fetchone()
            return rows

        except lite.Error as e:
            if con:
                con.rollback()
            print(f'Error: {e.args[0]}')
        finally:
            con.close()

    def update(self, table, values, conditions=None):
        sql_values = []
        sql = f"UPDATE {table} SET "

        if type(values) is tuple:
            sql += f"{values[0]}={values[1]}"
        elif type(values) is list:
            sql_values = [ f"{value[0]}='{value[1]}'" for value in values]
            sql_values = ", ".join(sql_values)
            sql += sql_values;

        if conditions:
            sql_conditions = []
            for condition in conditions:
                sql_conditions.append(f"{condition[0]}='{condition[1]}'")
            sql_conditions = " and ".join(sql_conditions)
            sql += " WHERE "+sql_conditions
        sql +=";"

        try:
            con = lite.connect(self.db_name)
            cur = con.cursor()
            print(sql)
            cur.execute(sql)
            con.commit()

        except lite.Error as e:
            if con:
                con.rollback()
            print(f'Error: {e.args[0]}')
        finally:
            con.close()
