from bottle import route, run, get, post, request, error, response, default_app, template, debug, static_file, Bottle
import json
import sessioncontroller as controller
import os
import sys

dirname = os.path.dirname(sys.argv[0])

app = Bottle()


@app.route('/static/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root=dirname + '/static/asset/css')


@app.route('/static/<filename:re:.*\.js>')
def send_js(filename):
    return static_file(filename, root=dirname + '/static/asset/js')


@app.route('/')
def index():
    return template('index')


@app.route('/teste')
def sensors():
    return controller.main()


app = default_app()
