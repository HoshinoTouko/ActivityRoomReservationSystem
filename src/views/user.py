'''User view model'''

from functools import wraps
from ..model import SubmitForm
from ..model.Common import Common
from ..model.Reservation import Reservation
from flask import Blueprint, session, request, render_template, redirect, url_for

USER = Blueprint('user', __name__)

def user_login_required(func):
    '''A decorated function that check if the user has logged in.'''
    @wraps(func)
    def decorated_function(*args, **kwargs):
        '''decorated_function'''
        if not is_login():
            return redirect(url_for('user.login', next=request.url))
        return func(*args, **kwargs)
    return decorated_function

def is_login():
    '''Check if the user has login'''
    if 'userIsLogin' in session.keys():
        if session['userIsLogin']:
            return True
    return False

@USER.route('/', methods=["GET", "POST"])
@user_login_required
def index():
    return render_template(
        'user/index.html'
    )

@USER.route('/login', methods=['GET', 'POST'])
def login():
    '''Login func'''
    if is_login():
        return redirect(url_for('user.index'))

    if request.method == 'POST':
        if Common.is_valid(request.form['username'], request.form['password']):
            session['username'] = request.form['username']
            session['userIsLogin'] = True
            return redirect(url_for('user.index'))
        else:
            return render_template('user/login.html', tip='用户名或者密码错误！')
    return render_template('user/login.html')
