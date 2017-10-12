'''Some common functions'''
import os
import hashlib


class Common:
    '''A class for handling common things'''
    @staticmethod
    def is_valid(username, password):
        '''Auth user'''
        # Gen a password list
        pass_file = open(str(os.path.abspath('src/data/pass.pass')))
        pass_dict = {}
        for line in pass_file.readlines():
            pass_dict[line.split()[0]] = line.split()[1]
            continue
        try:
            if pass_dict[username] == hashlib.sha3_512(password.encode()).hexdigest():
                return True
        except BaseException:
            return False
        return False

    @staticmethod
    def parse_date(date_text):
        '''Parse date text, like 30 August, 2017'''
        import time
        result = time.strptime(date_text, '%d %B, %Y')
        result_text = time.strftime('%Y-%m-%d', result)
        return result_text

    @staticmethod
    def get_date_range(area, offset=0):
        '''Return a list of a range of date string list.'''
        import datetime
        result = []
        now = datetime.datetime.now() + datetime.timedelta(days=offset)
        for i in range(0, area, 1 if area >= 0 else -1):
            result.append((now + datetime.timedelta(days=i)).strftime('%Y-%m-%d'))
        return result

    @staticmethod
    def list_filter(origin_list, key, value):
        '''A list filter'''
        result = []
        if not isinstance(value, list):
            value = [value]
        for item in origin_list:
            try:
                if item[key] in value:
                    result.append(item)
                    continue
                continue
            except BaseException:
                continue
        return result

    @staticmethod
    def json_beautify(original_obj):
        '''Beauty json data to strign(replace ' to ")'''
        return str(original_obj).replace("'", '"')
