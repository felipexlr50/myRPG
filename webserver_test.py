from bottle import route, run, get, post, request, error, response
import json


@route('/teste')
def sensors():
    return "teste"


run(host='0.0.0.0', port=8080, debug=True, server='paste', reloader=True)
