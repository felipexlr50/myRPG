from bottle import route, run, get, post, request, error, response, default_app, template, debug, static_file
import json
import sessioncontroller as controller
import os
import sys

dirname = os.path.dirname(sys.argv[0])


@route('/static/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root=dirname + '/static/asset/css')


@route('/static/<filename:re:.*\.js>')
def send_js(filename):
    return static_file(filename, root=dirname + '/static/asset/js')


@route('/teste')
def sensors():
    return controller.main()


application = default_app()
