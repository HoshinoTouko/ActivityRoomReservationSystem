'''A test model'''
from src.model.Common import Common
from src.model.User import User


def test_timeparser():
    '''Timeparser test function'''
    print('test_timeparser')
    print(Common.parse_date('30 August, 2017'))


def test_user():
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
    print('TEST: get_column_names\n' + str(db.get_column_names('Reservation')))
    print('TEST: select\n' + str(db.select('Reservation')))
    print('TEST: count\n' + str(db.count('Reservation', {'stuid': '2016300012345', 'status': 1})))
    print('TEST: find_max\n' + str(db.find_max('Reservation', 'id')))

def test_reservation():
    from src.model.Reservation import Reservation
    # print('TEST get_all_reservation\n' + str(Reservation.get_all_reservation()))
    # print('TEST get_date_range\n' + str(Common.get_date_range(10)))
    print('TEST get_past_reservation\n' + str(Reservation.get_past_reservation()))
    print('TEST get_future_reservation\n' + str(Reservation.get_future_reservation()))    

if __name__ == '__main__':
    test_timeparser()
    # test_user()
    # test_db()
    test_reservation()
