import mysuperclass


class Session(mysuperclass.RPGSuper):

    def __init__(self, sessionName, sessionOwnerId, description):
        self.sessionName = sessionName
        self.sessionId = self.toHashId(self)
        self.players = []
        self.master = None
        self.ownerId = sessionOwnerId
        self.users = []
        self.description = description
        self.progress = None
        self.npcs = []
        self.items = []
        self.skills = []
        self.quests = []

    def saveProgress(self, progress):
        self.progress = progress

    def getProgress(self):
        return self.progress

    def setPlayersConfig(self):
        for i in range(0, len(self.players)):
            self.players[i].setSessionId(self.sessionId)

    def setMasterConfig(self):
        self.master.setSessionId(self.sessionId)
        self.master.setPlayers(self.players)

    def getMasterConfig(self):
        self.players = self.master.getPlayers()
        self.quests = self.master.getQuests()
        self.items = self.master.getItems()
        self.skills = self.master.getSkills()
        self.npcs = self.master.getNpcs()

    def getDescription(self):
        return self.description

    def getName(self):
        return self.sessionName

    def getId(self):
        return self.sessionId

    def getOwnerId(self):
        return self.ownerId

    def addNpc(self, npc):
        self.npcs.append(npc)

    def getNpcs(self):
        return self.npcs

    def playersToJson(self):
        objList = []
        for i in range(0, len(self.players)):
            objList.append(self.players[i].toObject())

        return objList

    def questsToJson(self):
        objList = []
        for i in range(0, len(self.quests)):
            objList.append(self.quests[i].toObject())

        return objList

    def itemsToJson(self):
        objList = []
        for i in range(0, len(self.items)):
            objList.append(self.items[i].toObject())

        return objList

    def skillsToJson(self):
        objList = []
        for i in range(0, len(self.skills)):
            objList.append(self.skills[i].toObject())

        return objList

    def npcsToJson(self):
        objList = []
        for i in range(0, len(self.npcs)):
            objList.append(self.npcs[i].toObject())

        return objList

    def usersToJson(self):
        objList = []
        for i in range(0, len(self.users)):
            objList.append(self.users[i].toObject())

        return objList
