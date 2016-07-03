from rest_framework import serializers
import simplejson
from django.forms import model_to_dict


from models import *

def date_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        print 'issue : ' +str(obj)
        raise TypeError

class CustomSerializer():

    def __init__(self, objects):
        data = []
        for obj in objects:
            if not isinstance(obj, dict):
                obj = model_to_dict(obj)
            data.append(obj)

        self.data = data
