from gevent.pywsgi import WSGIServer


def app(environ, start_fn):
  data = b"Hello, Web!\n"
  start_fn('200 OK',[{'Content-Type', 'text/plain'}])
  return iter([data])


if __name__=="__main__":
  print("serving on 8000...")
  WSGIServer(('', 8000),app, spawn=None).serve_forever()