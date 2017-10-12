'''Index view module'''

from ..model import SubmitForm
from ..model.Common import Common
from ..model.Reservation import Reservation
from flask import Blueprint, session, request

API = Blueprint('api', __name__)

@API.route('/get_future_reservation', methods=["GET", "POST"])
def get_future_reservation():
    '''Get future 14days reservation'''
    return Common.json_beautify(Reservation.get_future_reservation())

@API.route('/get_past_reservation', methods=["GET", "POST"])
def get_past_reservation():
    '''Get past 14days reservation'''
    return Common.json_beautify(Reservation.get_past_reservation())

@API.route('/add_reservation', methods=["GET", "POST"])
def add_reservation():
    '''Backend check data and submit.'''
    return_data = {
        'status': 0,
        'data': [],
        'tip': ''
    }
    data = request.form.to_dict()
    if request.method == 'POST':
        # New a User
        user = SubmitForm.SubmitForm(data)
        # Log data
        print('API view get POST data:')
        user.show()
        # Reserve
        status, tip = user.check()
        # If check() passed, go to the next step
        if status == 1:
            status, tip = user.submit()
        # Set json
        return_data['status'] = 1 if status == 1 else -1
        return_data['tip'] = tip
    else:
        # If not POST method, set json
        return_data['status'] = 0
        return_data['tip'] = 'No POST data.'
        print('No POST data.')
    # Javascript cannot parse ', so you must replace it to "
    return Common.json_beautify(return_data)
