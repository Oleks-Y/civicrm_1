import requests


URL= "https://crm.meddata.com.ua/administrator/components/com_civicrm/civicrm/extern/rest.php"
APIKEY="80tP9MkrQFuAp36gXlXdGNEJ"
KEY="3e44b5d90bd9794c74b88b7f932aa50b"
def restCreate(dict):
    Data ={
        "entity" : "Activity",
        "action":"create",
        "api_key" : APIKEY,
        "key" : KEY,
        "json" : dict,
        "activity_type_id": 1,
        "is_test": True
    }
    response = requests.post(URL, data=Data)
    print(response.json())
    return response.json()