'''A model for user functions'''
from .db import DB

def auth_user_and_pass(username, password):
    '''Auth user by name and pass'''
    return True
    for item in data:
        if item['name'] == username and item['pass'] == password:
            return True
    return False
