from bottle import route, run, get, post, request, error, response, Bottle
import json
import sessioncontroller as controller
import os
import sys
#import bottle

app = Bottle()


@app.route('/teste')
def sensors():
    return controller.main()


#app.run(host='0.0.0.0', port=8080, debug=True, reloader=False)
