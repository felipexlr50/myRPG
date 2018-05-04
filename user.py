import mysuperclass
import db_connection as db


class User(mysuperclass.RPGSuper):

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.chars = []
        self.sessions = []
        self.id = self.toHashId(self)

    def getName(self):
        return self.name

    def getEmail(self):
        return self.email

    def addChars(self, charId):
        self.chars.append(charId)

    def addSession(self, session):
        self.sessions.append(session)

    def getUserId(self):
        return self.id

    def getPassword(self):
        return self.password

    def update(self, args):
        return db.update(self.id, args, "user")
