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
        self.conn.commit()
        self.conn.close()
        return cursor

    def update(self, table, data, target):
        '''Update function. data and target must be a dict.'''
        data_text = ''
        data_list = []
        target_text = ''
        target_list = []
        # Generate data text
        for key, value in data.items():
            temp = key + '='
            if isinstance(value, int) or isinstance(value, float):
                temp += '%s' % str(value)
            else:
                temp += '"%s"' % str(value)
            data_list.append(temp)
        data_text = ','.join(data_list)
        # Generate target text
        for key, value in target.items():
            temp = key + '='
            if isinstance(value, int) or isinstance(value, float):
                temp += '%s' % str(value)
            else:
                temp += '"%s"' % str(value)
            target_list.append(temp)
        target_text = ','.join(target_list)
        # Gen SQL
        sql = 'UPDATE `%s` SET %s WHERE %s' % (table, data_text, target_text)
        return self.run_sql(sql)

    def insert(self, table, data):
        '''Insert function. Data must be a list'''
        # If typeof data is dict, convert it to list
        if isinstance(data, dict):
            data = [data]
        # all data
        for item in data:
            # Init sql query
            sql = 'INSERT INTO `%s` VALUES ' % (table)
            values_list = []
            column_names = self.get_column_names(table)
            print(column_names)
            for key in column_names:
                # If not value, set it to ""
                try:
                    value = item[key]
                except BaseException:
                    value = ""
                if isinstance(value, int) or isinstance(value, float):
                    new_str = '%s' % str(value)
                else:
                    new_str = '"%s"' % str(value)

                values_list.append(new_str)
            sql += '(' + ', '.join(values_list) + ');'
            print(sql)
            self.run_sql(sql)

    def select(self, table):
        '''Select function'''
        if table == 'Reservation':
            sql = 'SELECT * FROM  `%s` ORDER BY reservdate DESC, id, starttime DESC, endtime DESC' % (table)
        else:
            sql = 'SELECT * FROM  `%s`' % (table)
        cursor = self.run_sql(sql)
        result = []
        # Get all column names in table
        column_names = self.get_column_names(table)
        return DB.column_filter(column_names, cursor)

    @staticmethod
    def column_filter(column_names, results):
        result = []
        for item in results:
            temp_dict = {}
            for num, column_name in enumerate(column_names):
                temp_dict[column_name] = item[num]
            result.append(temp_dict)
        return result

    def find_max(self, table, column):
        '''Get max data'''
        # Get data
        cursor = self.select(table)
        max_data = float(cursor[0][column])
        for item in cursor:
            max_data = max_data if float(item[column]) < max_data else float(item[column])
        return max_data

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
            is_match = True
            for key, value in data.items():
                if str(item[key]) == str(value):
                    continue
                else:
                    is_match = False
                    break
            count += 1 if is_match else 0
            continue
        return count
