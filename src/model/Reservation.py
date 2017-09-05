'''A model for reservation functions'''
import os
import datetime
import time
from .db import DB
from .Common import Common


class Reservation:
    '''A class about reservation handler.'''
    @staticmethod
    def change_status(reserv_id, status):
        '''Change the id of the reservation by id'''
        database = Reservation.get_db()
        return database.update(
            'Reservation', {
                'status': status
            }, {
                'id': reserv_id
            }
        )

    @staticmethod
    def get_future_reservation():
        '''Return a list about future 14 days reservation.'''
        return Common.list_filter(
            Reservation.get_all_reservation_safe(),
            'reservdate',
            Common.get_date_range(14)
        )

    @staticmethod
    def get_past_reservation():
        '''Return a list about past 14 days reservation.'''
        return Common.list_filter(
            Reservation.get_all_reservation_safe(),
            'reservdate',
            Common.get_date_range(-14)
        )

    @staticmethod
    def get_all_reservation_safe():
        '''Get a list about all reservation.'''
        database = Reservation.get_db()
        # For safety reason, delete phone column.
        result = database.select('Reservation')
        for item in result:
            del item['telephone']
        return result

    # Admin func

    @staticmethod
    def admin_get_future_reservation():
        '''Return a list about past 14 days reservation.'''
        return Common.list_filter(
            Reservation.get_all_reservation(),
            'reservdate',
            Common.get_date_range(14)
        )

    @staticmethod
    def get_all_reservation():
        '''Get a list about all reservation.'''
        database = Reservation.get_db()
        return database.select('Reservation')

    # DB func

    @staticmethod
    def get_db():
        '''Return a db class'''
        # Init database
        path = str(os.path.abspath('src/data/database.db'))
        # print (path)
        return DB(path)
