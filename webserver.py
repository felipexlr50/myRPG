from bottle import route, run, get, post, request, error, response, default_app
import json
import sessioncontroller as controller
import os
import sys


@route('/teste')
def teste():
    return controller.main()


application = default_app()
