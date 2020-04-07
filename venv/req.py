import requests
from vedis import Vedis
import ast
import config
import json

#superUserId=552
#usedId=553
URL= "https://crm.meddata.com.ua/administrator/components/com_civicrm/civicrm/extern/rest.php"
APIKEY="80tP9MkrQFuAp36gXlXdGNEJ"
KEY="3e44b5d90bd9794c74b88b7f932aa50b"
def restCreate(user):
    user_info_dict={"a":"1"}
    with Vedis(config.db_file_users) as db:

        user_info = db[user.id]
        user_info_dict = ast.literal_eval(user_info.decode("utf-8"))
        print(user_info_dict)
        dict={'source_record_id':str(user_info_dict["civi_id"]),
        'subject': str(user_info_dict["q"]),
        'details': str(user_info_dict["name"]+" "+user_info_dict["username"])}
        j= json.dumps(dict)
    Data ={
        "entity" : "Activity",
        "action":"create",
        "api_key" : APIKEY,
        "key" : KEY,
        "json" : j,
        "activity_type_id": 1,
        "is_test": True,

    }
    print(Data)
    response = requests.post(URL, data=Data)
    print(response.json())