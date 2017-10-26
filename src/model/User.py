import os
import hashlib
from .db import DB

class User:
    @staticmethod
    def auth(stuid, password):
        db = User.get_db()
        results = db.select('info')
        # print(results)
        # print(password)
        # print(hashlib.sha3_512(password.encode()).hexdigest())
        for item in results:
            if str(item.get('stuid')) == str(stuid):
                if item.get('pass') == hashlib.sha3_512(password.encode()).hexdigest():
                    print(item.get('pass'))
                    print(hashlib.sha3_512(password.encode()).hexdigest())
                    print('Auth pass')
                    return True
                else:
                    return False
        return False

    @staticmethod
    def update_pass(stuid, password):
        db = User.get_db()
        db.update(
            'info',
            {'pass': hashlib.sha3_512(password.encode()).hexdigest()},
            {'stuid': stuid}
        )

    @staticmethod
    def get_db():
        '''Return a db class'''
        # Init database
        path = str(os.path.abspath('src/data/StuInfo.db'))
        # print (path)
        return DB(path)
