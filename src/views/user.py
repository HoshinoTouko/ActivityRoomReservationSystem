'''User view model'''

from functools import wraps
from ..model import SubmitForm
from ..model.Common import Common
from ..model.Reservation import Reservation
from ..model.User import User
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
    print('User %s view his index page' % session['username'])
    tip = ''
    try:
        if request.method == 'POST':
            print(request.form)
            if request.form.get('do'):
                if request.form.get('do') == 'reset_password' and \
                        User.auth(session['username'], request.form.get('old_pass')):
                    User.update_pass(session['username'], request.form.get('new_pass'))
                    tip = '修改成功'
                else:
                    tip = '旧密码错误'
    except Exception as e:
        print(e)
        tip='未知错误'
    return render_template(
        'user/index.html',
        all_data=Reservation.get_reservation_by_stuid(session['username']),
        is_login=True,
        tip=tip
    )

@USER.route('/login', methods=['GET', 'POST'])
def login():
    '''Login func'''
    if is_login():
        return redirect(url_for('user.index'))
    if request.method == 'POST':
        if User.auth(request.form.get('username'), request.form.get('password')):
            session['username'] = request.form.get('username')
            session['userIsLogin'] = True
            return redirect(url_for('user.index'))
        else:
            return render_template(
                'user/login.html',
                stuid=request.form['username'],
                password=request.form['password'],
                tip='用户名或者密码错误！'
            )
    return render_template('user/login.html')
