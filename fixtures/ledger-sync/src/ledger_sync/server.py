"""Tiny status server, so the nightly job can be checked while it runs."""
from http.server import BaseHTTPRequestHandler, HTTPServer


class Health(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200 if self.path == "/health" else 404)
        self.end_headers()


def main():
    HTTPServer(("127.0.0.1", 8000), Health).serve_forever()
