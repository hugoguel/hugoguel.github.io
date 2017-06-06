# imports - standard imports
import os
import re
import uuid

def pardir(path, up = 1):
    for i in range(up):
        path = os.path.dirname(path)

    return path

def relurljoin(*args):
    construct = '/'.join([s for s in args])
    sanitized = re.sub('/+', '/', construct)

    return sanitized

def unique_id():
    objekt = uuid.uuid4()
    string = str(objekt)
    strip  = string.replace('-', '')

    return strip
