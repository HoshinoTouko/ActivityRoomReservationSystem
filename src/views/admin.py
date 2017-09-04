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
        if request.form['username'] == 'touko':
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
