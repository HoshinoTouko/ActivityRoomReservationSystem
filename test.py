'''A test model'''
from src.model.common import TimeParser
from src.model.userModel import Reservation


def test_timeparser():
    '''Timeparser test function'''
    print('test_timeparser')
    print(TimeParser.parse_date('30 August, 2017'))


def test_reservation():
    '''Reservation test func'''
    data_true = {
        'name': 'asdasd', 'telephone': '13612345678',
        'starttime': '08:00', 'endtime': '10:00',
        'reservdate': '30 August, 2017', 'room': '201',
        'forwhat': 'wkdfjenf'
    }
    data_false = {
        'name': 'asdasd', 'telephone': '136125678',
        'starttime': '08:00', 'endtime': '10:00',
        'reservdate': '30 August, 2017', 'room': '201',
        'forwhat': 'wkdfjenf'
    }
    print('test_reservation: True')
    print(Reservation.check_data(data_true))
    print('test_reservation: False')
    print(Reservation.check_data(data_false))


if __name__ == '__main__':
    test_timeparser()
    test_reservation()
