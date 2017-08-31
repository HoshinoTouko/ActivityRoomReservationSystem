'''A module for db connect'''
import sqlite3

class DB:
    '''A class for database connecting'''
    def __init__(self, dbpath):
        self.conn = sqlite3.connect(dbpath)
        self.dbpath = dbpath

    def run_sql(self, sql):
        '''Run SQL'''
        self.conn = sqlite3.connect(self.dbpath)
        conn_cursor = self.conn.cursor()
        cursor = list(conn_cursor.execute(sql))
        self.conn.close()
        return cursor

    def insert(self, table, data):
        '''Insert function. Data must be a list'''
        for item in data:
            columns_list = []
            values_list = []
            for key, value in item:
                columns_list.append(key)
                values_list.append(value)
            columns = ','.join(columns_list)
            values = ','.join(values_list)
            sql = 'INSERT INTO %s (%s) VALUES (%s)' % (table, columns, values)
            self.run_sql(sql)

    def select(self, table):
        '''Select function'''
        sql = 'SELECT * FROM  `%s` ORDER BY date, starttime, endtime DESC' % (table)
        cursor = self.run_sql(sql)
        result = []
        column_names = self.get_column_names(table)
        for item in cursor:
            temp_dict = {}
            for num, column_name in enumerate(column_names):
                temp_dict[column_name] = item[num]
            result.append(temp_dict)
        return result

    def get_column_names(self, table):
        '''Get all column names from table.'''
        sql = 'PRAGMA table_info(%s);' % table
        cursor = self.run_sql(sql)
        result = [x[1] for x in cursor]
        return result

    def count(self, table, data):
        '''Count function'''
        # Get data
        cursor = self.select(table)
        # Init count
        count = 0
        # Count
        for item in cursor:
            for key, value in data.items():
                if item[key] == value:
                    continue
                else:
                    break
            count += 1
            continue
        return count
