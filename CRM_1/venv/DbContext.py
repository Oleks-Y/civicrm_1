import datetime
import json
def write_response(response):
    path=r"response"+ str(datetime.datetime.now().time().microsecond)+".json"
    with open(path, 'w+') as f:
        f.write(json.dumps(str(response)))
