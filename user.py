import mysuperclass


class User(mysuperclass.RPGSuper):

    def __init__(self, username, email, userId):
        self.username = username
        self.email = email
        self.chars = []
        self.sessions = []
        self.userId = userId

    def getUsername(self):
        return self.username

    def getEmail(self):
        return self.email

    def addChars(self, charId):
        self.chars.append(charId)

    def addSession(self, session):
        self.sessions.append(session)

    def getUserId(self):
        return self.userId

    def setUserId(self, userId):
        self.userId = userId
