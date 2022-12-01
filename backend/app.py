import os
from http.server import HTTPServer, CGIHTTPRequestHandler

os.chdir('.')
# Create server object listening the port 80
server_object = HTTPServer(server_address=('', 8000), RequestHandlerClass=CGIHTTPRequestHandler)
server_object.serve_forever()
