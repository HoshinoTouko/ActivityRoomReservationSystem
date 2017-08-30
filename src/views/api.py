'''Index view module'''

from ..model import common, userModel
from flask import Blueprint, session, request

API = Blueprint('api', __name__)

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
        # Log data
        print('API view get POST data: ' + str(data))
        # Change date format
        data['reservdate'] = common.TimeParser.parse_date(data['reservdate'])
        # Reserve
        status, tip = userModel.Reservation.reserve(data)
        # Set json
        return_data['status'] = 1 if status else -1
        return_data['tip'] = tip
    else:
        # If not POST method, set json
        return_data['status'] = 0
        return_data['tip'] = 'No POST data.'
        print('No POST data.')
    # Javascript cannot parse ', so you must parse "
    return str(return_data).replace("'", '"')
