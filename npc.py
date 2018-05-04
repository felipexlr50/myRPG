import mysuperclass


class NPC(mysuperclass.RPGSuper):

    def __init__(self, id, name, job, race, story, sessionId):
        self.sessionId = sessionId
        self.creationDate = self.getDateNow()
        self.name = name
        self.job = job
        self.race = race
        self.story = story
        self.lvl = 1
        self.charId = id
        self.items = []
        self.skill = []

    def getName(self):
        return self.name

    def getJob(self):
        return self.job

    def getRace(self):
        return self.race

    def getStory(self):
        return self.story

    def addLvl(self, lvl):
        self.lvl += lvl

    def getLvl(self):
        return self.lvl

    def setSessionId(self, sessionId):
        self.sessionId = sessionId

    def getSession(self):
        return self.sessionId

    def addItem(self, item):
        self.items.append(item)

    def getItems(self):
        return self.items

    def addSkill(self, skill):
        self.skill.append(skill)

    def getSkills(self):
        return self.skill

    def getSkillById(self, skillId):
        return self.skill[skillId]
