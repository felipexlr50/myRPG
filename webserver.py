#from bottle import route, run, get, post, request, error, response, default_app, template, debug, static_file, Bottle
import json
import sessioncontroller as controller
import os
import sys
import bottle


dirname = os.path.dirname(sys.argv[0])

app = bottle.Bottle()

bottle.TEMPLATE_PATH.insert(0, 'view')


# Static Routes
@app.route("/static/css/<filepath:re:.*\.css>")
def css(filepath):
    return bottle.static_file(filepath, root="static/css")


@app.route("/static/font/<filepath:re:.*\.(eot|otf|svg|ttf|woff|woff2?)>")
def font(filepath):
    return bottle.static_file(filepath, root="static/font")


@app.route("/static/img/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return bottle.static_file(filepath, root="static/img")


@app.route("/static/js/<filepath:re:.*\.js>")
def js(filepath):
    return bottle.static_file(filepath, root="static/js")


@app.route('/')
def index():
    return bottle.template('index')


@app.route('/teste')
def sensors():
    return controller.main()


#app.run(host='0.0.0.0', port=8080, debug=True, reloader=False)
