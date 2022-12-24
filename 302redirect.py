#!/usr/bin/env python3

import sys
from http.server import HTTPServer, BaseHTTPRequestHandler

if len(sys.argv)-1 != 2:
    print("""
Usage: {} <2000> <https://bcc6-102-89-22-17.ngrok.io>
    """.format(sys.argv[0]))
    sys.exit()

class Redirect(BaseHTTPRequestHandler):
   def do_GET(self):
       self.send_response(302)
       self.send_header('Location', sys.argv[2])
       self.end_headers()
   def send_error(self, code, message=None):
       self.send_response(302)
       self.send_header('Location', sys.argv[2])
       self.end_headers()
HTTPServer(("", int(sys.argv[1])), Redirect).serve_forever()