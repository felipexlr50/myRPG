from bottle import route, run, get, post, delete, request, error, response, default_app
import json
import sessioncontroller as controller
import os
import sys
import hashkeyhandler as keyHandler

baseResponseObj = {'result': '', 'info': '', 'status-code': response.status}


@route('/<obj>')
@route('/<obj>/<id:path>')
def getObject(id=None, obj=None):
    response.content_type = 'application/json'
    #response.add_header('Access-Control-Allow-Origin', '*')
    print(obj)
    baseResponseObj['info'] = 'Found results'
    baseResponseObj['status-code'] = response.status
    result = None

    if(id):
        result = controller.getObject(
            id=id, condition="where id = '"+str(id)+"'", interface=obj)
        baseResponseObj['result'] = result
    elif(request.query):
        # TODO
        print("")
    else:
        result = controller.getObject(interface=obj)
        baseResponseObj['result'] = result

    if(not result):
        response.status = 202
        baseResponseObj['result'] = 'No results'
        baseResponseObj['info'] = 'No results found'
        baseResponseObj['status-code'] = response.status
    return json.dumps(baseResponseObj)


@route('/users/<user:path>', method='PATCH')
def patchUser(user=None):
    return "PATCH"


@route('/<obj>/<user:path>', method='DELETE')
def deleteObject(user=None):
    return "DELETE"


@route('/users', method='POST')
def newUser(obj=None):
    response.content_type = 'application/json'
   # response.add_header('Access-Control-Allow-Origin', '*')
    newUserJson = request.json
    key = request.get_header('key')

    if(newUserJson and keyHandler.isRequestOK(key)):
        newUserObj = newUserJson
        result, user = controller.newUser(
            newUserObj['name'], newUserObj['email'], newUserObj['password'])
        if(result):
            baseResponseObj['result'] = 'OK'
            baseResponseObj['info'] = 'user ' + \
                str(user.getName()) + " created!"
            baseResponseObj['status-code'] = response.status
            return json.dumps(baseResponseObj)
        else:
            response.status = 500
            baseResponseObj['result'] = 'FAULT'
            baseResponseObj['info'] = 'Failed user creation'
            baseResponseObj['status-code'] = response.status
            return json.dumps(baseResponseObj)
    else:
        response.status = 400
        baseResponseObj['result'] = 'NOT ALLOWED'
        baseResponseObj['info'] = 'Missing or wrong body request'
        baseResponseObj['status-code'] = response.status
        return json.dumps(baseResponseObj)


@route('/sessions', method='POST')
def newSession(obj=None):
    response.content_type = 'application/json'
   # response.add_header('Access-Control-Allow-Origin', '*')
    newJson = request.json
    key = request.get_header('key')

    if(newJson):
        newObj = newJson
        result, session = controller.newSession(
            newObj['ownerId'], newObj['name'], newObj['description'])
        if(result):
            baseResponseObj['result'] = 'OK'
            baseResponseObj['info'] = 'Session ' + \
                str(session.getName()) + " created!"
            baseResponseObj['status-code'] = response.status
            return json.dumps(baseResponseObj)
        else:
            response.status = 500
            baseResponseObj['result'] = 'FAULT'
            baseResponseObj['info'] = 'Failed session creation'
            baseResponseObj['status-code'] = response.status
            return json.dumps(baseResponseObj)
    else:
        response.status = 400
        baseResponseObj['result'] = 'NOT ALLOWED'
        baseResponseObj['info'] = 'Missing or wrong body request'
        baseResponseObj['status-code'] = response.status
        return json.dumps(baseResponseObj)


application = default_app()
application.run(host='0.0.0.0', port=8080, debug=True, reloader=False)
