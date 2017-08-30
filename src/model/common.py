'''Some common functions'''

class TimeParser:
    '''A class for resolve time and date text'''
    @staticmethod
    def parse_date(date_text):
        '''Parse date text, like 30 August, 2017'''
        import time
        result = time.strptime(date_text, '%d %B, %Y')
        result_text = time.strftime('%Y-%m-%d', result)
        return result_text
