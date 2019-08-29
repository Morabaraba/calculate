from flask.json import JSONEncoder
from decimal import Decimal

class DecimalEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return f'{obj}'
        return JSONEncoder.default(self, obj) # default
