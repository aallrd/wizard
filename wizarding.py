#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import base64
import gzip
import zlib
from io import StringIO
from subprocess import check_output

HOSTNAME = "0.0.0.0"
PORT = 1337

def getEncodedWizardSystem():
    base64_wizard = None
    with open('wizard.ascii', 'r', encoding='utf-8') as f:
        wizard = bytes(f.read(), 'utf-8')
        gzipped_wizard = gzip.compress(wizard)
        base64_wizard = base64.b64encode(gzipped_wizard)
    return base64_wizard

# Should be the same as cat wizard.ascii | gzip | openssl enc -base64
# Working on Solaris, not on Linux somehow...
def getEncodedWizard():
    encoded = StringIO()
    with open('wizard.ascii', 'r') as wizard:
        with gzip.GzipFile(fileobj=encoded, mode="w") as gzipped:
            gzipped.write(wizard.read())
    return base64.b64encode(encoded.getvalue())

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(s):
        s.send_response(200)
        s.send_header("Content-type", "text/plain")
        s.end_headers()
        s.wfile.write(getEncodedWizardSystem())

if __name__ == '__main__':
    http_server = HTTPServer((HOSTNAME, PORT), MyHandler)
    http_server.serve_forever()
