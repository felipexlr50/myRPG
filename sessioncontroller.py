import session
import player
import master
import user
import json
import db_connection as db


def newUser(name, email, password):
    userObj = user.User(name, email, password)
    args = []
    args.append({'name': "id", 'value': userObj.getId()})
    args.append({'name': "name", 'value': userObj.getName()})
    args.append({'name': "email", 'value': userObj.getEmail()})
    args.append({'name': "password", 'value': userObj.getPassword()})
    return db.insert("user", args), userObj


def newSession(ownerId, name,  description):
    obj = session.Session(name, ownerId, description)
    args = []
    args.append({'name': "id", 'value': obj.getId()})
    args.append({'name': "ownerId", 'value': obj.getOwnerId()})
    args.append({'name': "name", 'value': obj.getName()})
    args.append({'name': "description", 'value': obj.getDescription()})
    return db.insert("session", args), obj


def newMaster(userId, sessionId):
    obj = master.Master(userId, sessionId)
    args = []
    args.append({'name': "id", 'value': obj.getId()})
    args.append({'name': "userId", 'value': obj.getMasterUserId()})
    args.append({'name': "sessionId", 'value': obj.getSessionId()})

    return db.insert("master", args), obj


def newPlayer(name, gender, job, race, story, sessionId, userId):
    obj = player.Player(name, gender, job, race, story, sessionId, userId)
    args = []
    args.append({'name': "id", 'value': obj.getId()})
    args.append({'name': "name", 'value': obj.getName()})
    args.append({'name': "gender", 'value': obj.getGender()})
    args.append({'name': "job", 'value': obj.getJob()})
    args.append({'name': "race", 'value': obj.getRace()})
    args.append({'name': "story", 'value': obj.getStory()})
    args.append({'name': "sessionId", 'value': obj.getSessionId()})
    args.append({'name': "userId", 'value': obj.getUserId()})

    return db.insert("player", args), obj


def getObject(id=None, fields=None, condition=None, interface=None):
    table = db.getMapTables(interface)
    args = {'fields': fields, 'condition': condition}
    data, fieldsDb = db.select(table, args)
    return dataToJson(data, fieldsDb, table)


def dataToJson(data, fields, table):
    objArray = []
    if(data):
        for row in data:
            obj = {}
            i = 0
            for field in fields:
                obj[field] = str(row[i])
                i += 1
            objArray.append(obj)

        return {table: objArray}
    else:
        return False
