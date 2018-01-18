import mysuperclass


class Master(mysuperclass.RPGSuper):

    def __init__(self, players, quests, items, skills, npcs, sessionId):

        self.players = players
        self.quests = quests
        self.items = items
        self.skills = skills
        self.npcs = npcs
        self.sessionId = sessionId

    def setPlayers(self, players):
        self.players = players

    def addPlayer(self, player):
        self.players.append(player)

    def removePlayer(self, player):
        playerid = self.players.index(player)
        self.players.pop(playerid)

    def getPlayers(self):
        return self.players

    def addQuest(self, quest):
        self.quests.append(quest)

    def getQuests(self):
        return self.quests

    def addItem(self, item):
        self.items.append(item)

    def getItems(self):
        return self.items

    def addSkill(self, skill):
        self.skills.append(skill)

    def getSkills(self):
        return self.skills

    def addNpc(self, npc):
        self.npcs.append(npc)

    def getNpcs(self):
        return self.npcs

    def setSessionId(self, sessionId):
        self.sessionId = sessionId

    def getSessionId(self):
        return self.sessionId
