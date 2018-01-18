import mysuperclass


class Quest(mysuperclass.RPGSuper):

    def __init__(self, name, objective, description, reward):
        self.name = name
        self.objective = objective
        self.description = description
        self.reward = reward

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setObjective(self, objective):
        self.objective = objective

    def getObjective(self):
        return self.objective

    def setDescription(self, description):
        self.description = description

    def getDescription(self):
        return self.description

    def setReward(self, reward):
        self.reward = reward

    def getReward(self):
        return self.reward
