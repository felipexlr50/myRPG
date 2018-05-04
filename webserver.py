from bottle import route, run, get, post, delete, request, error, response, default_app
import json
import sessioncontroller as controller
import os
import sys


@route('/users')
@route('/users/<user:path>')
def getUser(user=None):
    return "GET"+str(user)


@route('/users/<user:path>', method='PUT')
@route('/users/<user:path>', method='PATCH')
def patchUser(user=None):
    return "PATCH"


@route('/users/<user:path>', method='DELETE')
def deleteUser(user=None):
    return "DELETE"


@route('/users', method='POST')
def newUser():
    response.content_type = 'application/json'
    response.add_header('Access-Control-Allow-Origin', '*')
    newUserJson = request.json

    if(newUserJson):
        newUserObj = newUserJson
        result, user = controller.newUser(
            newUserObj['name'], newUserObj['email'], newUserObj['password'])
        if(result):
            return json.dumps({'result': 'OK', 'info': 'user ' + str(user.getName()) + " created!"})
        else:
            return json.dumps({'result': 'FAULT', 'info': 'Failed user creation'})
    else:
        return "Not POST"


application = default_app()
application.run(host='0.0.0.0', port=8080, debug=True, reloader=False)
