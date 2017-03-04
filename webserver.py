from http.server import BaseHTTPRequestHandler, HTTPServer

class wordHttpServer(BaseHTTPRequestHandler):

    def do_GET(self):

        # set header
        self.send_response(200)

        self.send_header('Content-type', 'text/html')

        self.end_headers()

        message = 'hello world!!'

        self.wfile.write(bytes(message, "utf8"))

        return

def run():

    print('starting server...')

    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = ('127.0.0.1', 8081)

    httpd = HTTPServer(server_address, wordHttpServer)

    print('running server...')

    httpd.serve_forever()

run()