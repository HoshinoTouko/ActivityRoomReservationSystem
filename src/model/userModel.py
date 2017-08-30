'''A model for user functions'''
from .db import DB
from .common import TimeParser


class Reservation:
    '''A class to resolve reservation request'''
    @staticmethod
    def check_data(data):
        '''Check if the data is valid'''
        import re
        '''
        Sample data
        {
            'name': 'asdasd', 'telephone': '123213',
            'starttime': '08:00', 'endtime': '10:00',
            'reservdate': '30 August, 2017', 'room': '201',
            'forwhat': 'wkdfjenf'
        }
        '''
        regularly_list = {
            'name': '^[\u4E00-\u9FA5A-Za-z0-9]+$',
            'telephone': '^(1[3|4|5|6|7|8|9])\d{9}$',
            'starttime': '^\d{2}:\d{2}',
            'endtime': '^\d{2}:\d{2}',
            'reservdate': '^\d{4}-\d{1,2}-\d{1,2}',
            'room': '^[\u4E00-\u9FA5A-Za-z0-9]+$',
            'forwhat': '^[\u4E00-\u9FA5A-Za-z0-9]+$'
        }
        keyname_list = {
            'name': '名字',
            'telephone': '电话',
            'starttime': '开始时间',
            'endtime': '结束时间',
            'reservdate': '预定日期',
            'room': '房间',
            'forwhat': '用途'
        }
        for key in data.keys():
            valid = False
            try:
                valid = re.match(regularly_list[key], data[key])
            except BaseException as error:
                valid = False
                print('Regular parse error: ' + str(error))

            if valid:
                continue
            else:
                return False, keyname_list[key] + '出错啦'
        return True, 'OK'

    @staticmethod
    def reserve(data):
        '''Reserve room'''
        status, tip = Reservation.check_data(data)
        if status:
            pass
        return status, tip

    @staticmethod
    def auth_user(username, authinfo):
        '''Auth user by name and pass'''
        return True
