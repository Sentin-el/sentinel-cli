from json import dumps

from bottle import Bottle, run
from paste import httpserver
from bottle import response

from sentinel.scripts.top import top

sentinel_app = Bottle()


@sentinel_app.route('/hello')
def test_server():
    response.content_type = 'application/json'
    top()
    return dumps([{"name": "hello_world"}])


httpserver.serve(sentinel_app, host='0.0.0.0', port=80)
