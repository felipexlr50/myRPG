import json
import hashlib as hash
import datetime


class RPGSuper(object):

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=False, indent=4)

    def toObject(self):
        return json.loads(self.toJSON())

    def toHashId(self, obj):
        return hash.sha224(bytes(str(obj), 'utf-8')).hexdigest()

    def getDateNow(self):
        return str(datetime.datetime.now())
