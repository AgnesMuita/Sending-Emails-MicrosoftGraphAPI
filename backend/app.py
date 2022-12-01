import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler, test
from index import send_email

class CORSRequestHandler (SimpleHTTPRequestHandler):
    def add_headers (self):
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)
        send_email()

if __name__ == '__main__':
    test(CORSRequestHandler, HTTPServer, port=int(sys.argv[1]) if len(sys.argv) > 1 else 5000)
