from vedis import Vedis
import config
import json
import ast

def setNewUser(user, id):
    with Vedis(config.db_file_users) as db:
        db[user.id] = { "name": user.first_name+user.last_name,
                        "username" : user.username,
                        "civi_id" : id,
                        "q":""
                        }
def addQuestion(user,q):
    with Vedis(config.db_file_users) as db:
        print(db[user.id])
        user_info=db[user.id]
        print(user_info.decode("utf-8"))

        user_info_dict = ast.literal_eval(user_info.decode("utf-8"))
        user_info_dict["q"]=q
        db[user.id]=user_info_dict
        print(user_info_dict)
def delinfo(user):
    with Vedis(config.db_file_users) as db:
        db.delete(user.id)

