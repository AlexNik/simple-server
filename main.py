import http.server
import socketserver

PORT = 8000


class Handler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200, 'OK')
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        print(self.request)

        self.wfile.write(self.headers.as_bytes())


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
