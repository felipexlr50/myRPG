import mysuperclass


class Player(mysuperclass.RPGSuper):

    def __init__(self, name, job, race, story, sessionId, userId):
        self.sessionId = sessionId
        self.userId = userId
        self.creationDate = self.getDateNow()
        self.name = name
        self.job = job
        self.race = race
        self.story = story
        self.exp = 0
        self.lvl = 1
        self.charId = self.toHashId(self)
        self.quest = []
        self.items = []
        self.skill = []
        self.statusPoint = 0
        self.status = {'STR': 0, 'PER': 0, 'END': 0,
                       'CHA': 0, 'INT': 0, 'AGI': 0, 'LUK': 0}

    def getName(self):
        return self.name

    def getJob(self):
        return self.job

    def getRace(self):
        return self.race

    def getStory(self):
        return self.story

    def addExp(self, exp):
        self.exp += exp

    def getExp(self):
        return self.exp

    def addLvl(self, lvl):
        self.lvl += lvl

    def getLvl(self):
        return self.lvl

    def setQuest(self, quest):
        self.quest = quest

    def getQuests(self):
        return self.quest

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

    def setStatus(self, STR=None, PER=None, END=None,
                  CHA=None, INT=None, AGI=None, LUK=None):

        if(STR is not None):
            self.status['STR'] = STR

        if(PER is not None):
            self.status['PER'] = PER

        if(END is not None):
            self.status['END'] = END

        if(CHA is not None):
            self.status['CHA'] = CHA

        if(INT is not None):
            self.status['INT'] = INT

        if(AGI is not None):
            self.status['AGI'] = AGI

        if(LUK is not None):
            self.status['LUK'] = LUK

    def addStatus(self, STR=None, PER=None, END=None,
                  CHA=None, INT=None, AGI=None, LUK=None):

        if(STR is not None):
            self.status['STR'] += STR

        if(PER is not None):
            self.status['PER'] += PER

        if(END is not None):
            self.status['END'] += END

        if(CHA is not None):
            self.status['CHA'] += CHA

        if(INT is not None):
            self.status['INT'] += INT

        if(AGI is not None):
            self.status['AGI'] += AGI

        if(LUK is not None):
            self.status['LUK'] += LUK

    def setStatusPoint(self, point):
        self.statusPoint = point

    def addStatusPoint(self, point):
        self.statusPoint += point

    def getStatusPoint(self):
        return self.setStatusPoint

    def getUserId(self):
        return self.userId

    def setUserId(self, userId):
        self.userId = userId
