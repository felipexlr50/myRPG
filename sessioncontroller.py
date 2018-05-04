import session
import player
import master
import user
import json
import db_connection as db


def newUser(name, email, password):
    userObj = user.User(name, email, password)
    args = []
    args.append({'name': "id", 'value': userObj.getUserId()})
    args.append({'name': "name", 'value': userObj.getName()})
    args.append({'name': "email", 'value': userObj.getEmail()})
    args.append({'name': "password", 'value': userObj.getPassword()})
    return db.insert("user", args), userObj


def getUser(id=None, fields=None, condition=None):
    args = {'fields': fields, 'condition': condition}
