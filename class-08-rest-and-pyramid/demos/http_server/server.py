from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from cowpy import cow
import json
import sys
import os


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        parsed_qs = parse_qs(parsed_url.query)

        if parsed_url.path == '/':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Try something like this: http http://127.0.0.1:5000/cow?msg="hello world"')

        elif parsed_url.path == '/cow':
            c = cow.Beavis()

            try:
                msg = c.milk(parsed_qs['msg'][0])
            except KeyError:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'Bad Request. Query options must include message')
                return

            self.send_response(200)
            self.end_headers()
            self.wfile.write(str.encode(msg))

        elif parsed_url.path == '/test':
            self.send_response(302)
            self.end_headers()
            self.wfile.write(b'test endpoint')

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

    def do_POST(self):
        parsed_url = urlparse(self.path)

        if parsed_url.path == '/cow':
            content_length = int(self.headers['Content-Length'])
            body = json.loads(self.rfile.read(content_length).decode('utf8'))
            print(body['msg'])

            self.send_response(201)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()

            c = cow.Beavis()
            msg = c.milk(body['msg'])

            self.wfile.write(str.encode(json.dumps({"content": msg})))

        else:
            self.send_response(404)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(b'''
                <!DOCTYPE html>
                <html>
                <head>
                    <title> cowsay </title>
                </head>
                <body>
                    <h1> cowsay </h1>
                    <pre>
                    <!-- cowsay.say({text: req.query.text}) -->
                    </pre>
                </body>
                </html>
            ''')


def create_server():
    return HTTPServer(('127.0.0.1', int(os.environ.get('PORT', 5000))), SimpleHTTPRequestHandler)


def run_forever():
    httpd = create_server()

    try:
        print('Starting server on 127.0.0.1:{}'.format(os.environ.get('PORT', 5000)))
        httpd.serve_forever()
    except KeyboardInterrupt:
        sys.exit()


if __name__ == '__main__':
    run_forever()
