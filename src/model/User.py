'''A model for user functions'''
from .db import DB
from .Common import TimeParser


class User:
    '''This is a class for handling user data.'''

    def __init__(self, data):
        # Init class variable
        self.info = {}
        self.is_valid = False
        self.tip = ''
        # If the data is a list
        if isinstance(data, list):
            for offset in range(len(self.user_keys)):
                self.info[self.user_keys[offset]] = data[offset]
        # Else if the data is a dictionary
        elif isinstance(data, dict):
            for offset in range(len(self.user_keys)):
                key = self.user_keys[offset]
                self.info[key] = data[key]
        # Convert date format
        self.info['reservdate'] = TimeParser.parse_date(self.info['reservdate'])
        # Check it
        self.is_valid, self.tip = self.check()

    def submit():
        '''Submit user '''

    def check(self):
        '''Check if the user is valid'''
        import re
        data = self.info
        # print(data)
        for key in data:
            valid = False
            try:
                valid = re.match(self.regularly_list[key], data[key])
            except BaseException as error:
                valid = False
                print('Regular parse error: ' + str(error))

            if valid:
                continue
            else:
                return False, self.keyname_list[key] + '出错啦'
        return True, 'OK'

    def show(self):
        '''Print user info at console'''
        print(self.info)

    regularly_list = {
        'name': '^[\u4E00-\u9FA5A-Za-z0-9]+$',
        'telephone': '^(1[3|4|5|6|7|8|9])\d{9}$',
        'stuid': '^(201[4|5|6|7|8|9])\d{9}$',
        'password': '^[\u4E00-\u9FA5A-Za-z0-9]+$',
        'starttime': '^\d{2}:\d{2}',
        'endtime': '^\d{2}:\d{2}',
        'reservdate': '^\d{4}-\d{1,2}-\d{1,2}',
        'room': '^[\u4E00-\u9FA5A-Za-z0-9]+$',
        'forwhat': '^[\u4E00-\u9FA5A-Za-z0-9]+$'
    }
    keyname_list = {
        'name': '名字',
        'telephone': '电话',
        'stuid': '学号',
        'password': '密码',
        'starttime': '开始时间',
        'endtime': '结束时间',
        'reservdate': '预定日期',
        'room': '房间',
        'forwhat': '用途'
    }
    user_keys = [
        'name',
        'telephone',
        'stuid',
        'password',
        'starttime',
        'endtime',
        'reservdate',
        'room',
        'forwhat'
    ]


class Reservation:
    '''A class to resolve reservation request'''
