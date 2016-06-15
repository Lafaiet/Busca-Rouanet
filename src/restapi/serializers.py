from rest_framework import serializers
import simplejson

from models import *

def date_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        print 'issue : ' +str(obj)
        raise TypeError

class CustomSerializer():

    def __init__(self, objects, total):
        rows = list(objects)
        self.data = simplejson.dumps({'total': total, 'rows': rows}, default=date_handler)
