import mysuperclass


class Skill(mysuperclass.RPGSuper):

    def __init__(self, idSkill, skillName, description, values):
        self.idSkill = idSkill
        self.skillName = skillName
        self.description = description
        self.values = values

    def setSkillName(self, skillName):
        self.skillName = skillName

    def getSkillName(self):
        return self.skillName

    def setDescription(self, description):
        self.description = description

    def getDescription(self):
        return self.description

    def setValues(self, values):
        self.values = values

    def getValues(self):
        return self.values
