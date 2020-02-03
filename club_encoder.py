from json import *
from club import Club

class ClubEncoder(JSONEncoder):
     def default(self, obj):
        if isinstance(obj, Club):
            return {"Club Name: " : obj.get_name(),
            "Club Tags" : obj.get_category(),
            "Club Description" : obj.get_descr(),
            "Club Favorite Count" : obj.get_fav()}
        return JSONEncoder.default(self, obj)