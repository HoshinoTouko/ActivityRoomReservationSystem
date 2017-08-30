'''Index view module'''

from flask import Blueprint, render_template, session, request

API = Blueprint('api', __name__)

@API.route('/add_reservation', methods=["GET", "POST"])
def add_reservation():
    '''Do some stuff'''
    print(request.form["name"])
    if request.method == 'POST':
        return str(request.form)
    return 'Nothing'
