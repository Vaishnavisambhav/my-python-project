import datetime
import os
import json

def date_time():
    today_date = datetime.date.today()
    return today_date

def current_directory():
    cur_dir=os.getcwd()
    return cur_dir

def to_json(data=None):
    if data is None:
        data = {}
    json_string = json.dumps(data)
    return json_string

print(date_time())
print(current_directory())

data = {"name":"vaish","age":24}
print(to_json(data))