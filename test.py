'''A test model'''
from src.model.Common import TimeParser
from src.model.User import User


def test_timeparser():
    '''Timeparser test function'''
    print('test_timeparser')
    print(TimeParser.parse_date('30 August, 2017'))


def test_reservation():
    '''Reservation test func'''
    data_true = {
        'name': '正确的信息', 'telephone': '13612345678',
        'stuid': '2016300012345', 'password': 'sfjsafbjksdf',
        'starttime': '08:00', 'endtime': '10:00',
        'reservdate': '30 August, 2017', 'room': '201',
        'forwhat': 'wkdfjenf'
    }
    data_false = {
        'name': 'asdasd', 'telephone': '136125678',
        'stuid': '2016300012345', 'password': 'sfjsafbjksdf',
        'starttime': '08:00', 'endtime': '10:00',
        'reservdate': '30 August, 2017', 'room': '201',
        'forwhat': 'wkdfjenf'
    }
    user_true = User(data_true)
    user_false = User(data_false)
    print('test_reservation: True')
    user_true.show()
    print(user_true.check())
    user_false.show()
    print('test_reservation: False')
    print(user_false.check())

def test_db():
    from src.model.db import DB
    db = DB('src/data/database.db')
    print(db.get_column_names('Reservation'))
    print(db.select('Reservation'))
    print(db.count('Reservation', {'stuid': '2016300012345'}))

if __name__ == '__main__':
    test_timeparser()
    # test_reservation()
    test_db()
