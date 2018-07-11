'''voluptuous包'''
from voluptuous import *
def convert_letter(value):
    if isinstance(value, str):
        return value.upper()
    raise Invalid("not valid string")
 
transformation_s = Schema({
    Required('key'): convert_letter,
    'per_page': int,
    'page': int
})
 
print(transformation_s({'key': 'hass'}))
'''{'key': 'HASS'}'''

'''如：Required('key'): convert_letter,此句中convert_letter可为方法名；
可为标量如12，'hass'等；
可为数据类型'''