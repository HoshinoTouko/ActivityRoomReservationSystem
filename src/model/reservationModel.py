'''A model for fetch or pull posts'''
import markdown
from .db import DB

# Get method
def get_reservation_by_id(post_id):
    '''Get posts of one author'''
    return list_filter(get_all_reservation(), 'id', post_id)

def get_all_reservation():
    '''Get all reservation from database'''
    database = DB()
    post_data = database.select('reservation')
    all_post_data = []
    for item in post_data:
        print(item)
        post_data = {
            'id': item[0],
            'name': item[1],
            'tel': item[2],
            'date': item[3],
            'starttime': item[4],
            'endtime': item[5],
            'forwhat': item[6],
            'room': item[7],
            'status': item[8]
        }
        all_post_data.append(post_data)
    return all_post_data

def list_filter(original_list, key, value):
    '''A filter for filtering key and value'''
    result = []
    for item in original_list:
        if item[key] == value:
            result.append(item)
    return result
