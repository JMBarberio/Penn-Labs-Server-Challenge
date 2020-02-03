from json import *
from user import User

class UserEncoder(JSONEncoder):
     def default(self, obj):
        if isinstance(obj, User):
            return {"User Name: " : obj.get_user_name(),
            "User Clubs" : obj.get_user_clubs()}
        return JSONEncoder.default(self, obj)