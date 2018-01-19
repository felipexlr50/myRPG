from bottle import route, run, get, post, request, error, response, default_app
import json
import sessioncontroller as controller


@route('/teste')
def sensors():
    return controller.main()


application = default_app()
