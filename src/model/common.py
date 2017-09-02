'''Some common functions'''


class Common:
    '''A class for handling date'''
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
            continue
        return result
