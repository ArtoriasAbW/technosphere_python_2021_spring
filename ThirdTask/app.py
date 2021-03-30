from datetime import datetime
import json

def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    cur_time = datetime.now()
    data = {"time": str(cur_time), "url": environ['HTTP_HOST']}
    tmp_str = json.dumps(data)
    binary = str.encode(tmp_str)
    yield binary
