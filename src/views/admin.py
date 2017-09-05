'''Index view module'''

from functools import wraps
from ..model import Common, User, Reservation
from flask import Blueprint, session, request, render_template, redirect, url_for
Common = Common.Common
Reservation = Reservation.Reservation

ADMIN = Blueprint('admin', __name__)

def login_required(func):
    '''A decorated function that check if the user has logged in.'''
    @wraps(func)
    def decorated_function(*args, **kwargs):
        '''decorated_function'''
        if not is_login():
            return redirect(url_for('admin.login', next=request.url))
        return func(*args, **kwargs)
    return decorated_function

def is_login():
    '''Check if the user has login'''
    if 'isLogin' in session.keys():
        if session['isLogin']:
            return True
    return False

# -------------------------------------------------------------------------------------
# Route
# -------------------------------------------------------------------------------------
@ADMIN.route('/api/pass_reservation', methods=["GET", "POST"])
@login_required
def pass_reservation():
    '''Pass the reservation'''
    if request.method == 'POST':
        try:
            Reservation.change_status(request.form['id'], 1)
        except BaseException:
            return '0'
    return '1'

@ADMIN.route('/api/pend_reservation', methods=["GET", "POST"])
@login_required
def pend_reservation():
    '''Let the reservation be pended'''
    if request.method == 'POST':
        try:
            Reservation.change_status(request.form['id'], 0)
        except BaseException:
            return '0'
    return '1'

@ADMIN.route('/api/refuse_reservation', methods=["GET", "POST"])
@login_required
def refuse_reservation():
    '''Refuse the reservation'''
    if request.method == 'POST':
        try:
            Reservation.change_status(request.form['id'], -1)
        except BaseException:
            return '0'
    return '1'

@ADMIN.route('/manage_future', methods=["GET", "POST"])
@login_required
def manage_future():
    '''Manage future reservation.'''
    data = Reservation.admin_get_future_reservation()
    result = {}
    result_reverse = {}
    for item in data:
        try:
            result[item['reservdate']].append(item)
        except BaseException:
            result[item['reservdate']] = [item]
    for key in list(result.keys())[::-1]:
        result_reverse[key] = result[key]
    return render_template('admin/manage_future.html', all_data=result_reverse, is_login=True)

@ADMIN.route('/api/manage_future', methods=["GET", "POST"])
@login_required
def api_manage_future():
    '''Manage future reservation.'''
    data = Reservation.admin_get_future_reservation()
    result = {}
    result_reverse = {}
    for item in data:
        try:
            result[item['reservdate']].append(item)
        except BaseException:
            result[item['reservdate']] = [item]
    for key in list(result.keys())[::-1]:
        result_reverse[key] = result[key]
    return Common.json_beautify(result_reverse)

@ADMIN.route('/get_all', methods=["GET", "POST"])
@login_required
def get_all():
    '''Show all reservation'''
    return render_template('admin/get_all.html', is_login=True, all_data=Reservation.get_all_reservation())

@ADMIN.route('/')
@login_required
def index():
    '''Admin page'''
    return render_template('admin/admin.html', is_login=True)

@ADMIN.route('/login', methods=['GET', 'POST'])
def login():
    '''Login func'''
    if is_login():
        return redirect(url_for('admin.index'))

    if request.method == 'POST':
        if Common.is_valid(request.form['username'], request.form['password']):
            session['username'] = request.form['username']
            session['isLogin'] = True
            return redirect(url_for('admin.index'))
        else:
            return render_template('admin/login.html', tip='用户名或者密码错误！')
    return render_template('admin/login.html')

@ADMIN.route('/logout')
def logout():
    '''Log out func'''
    session.pop('username', None)
    session['isLogin'] = False
    return redirect(url_for('admin.login'))
