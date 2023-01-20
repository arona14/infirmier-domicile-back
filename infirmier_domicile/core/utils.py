import json
import datetime
from bson import ObjectId


class MJSONEncoder(json.JSONEncoder):
    """
    Extend json-encoder class to handle mongo objectIds and datetime as well
    """

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)
