import mysuperclass


class Item(mysuperclass.RPGSuper):

    def __init__(self, name, description, type, allow, value):
        self.name = name
        self.description = description
        self.type = type
        self.allow = allow
        self.value = value

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setDescription(self, description):
        self.description = description

    def getDescription(self):
        return self.description

    def setType(self, type):
        self.type = type

    def getType(self):
        return self.type

    def setAllow(self, allow):
        self.allow = allow

    def getAllow(self):
        return self.allow

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value
