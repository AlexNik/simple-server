import datetime
import http.server
import socketserver

PORT = 8000


class Handler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200, 'OK')
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        print(self.request)

        for k, v in self.headers.items():
            self.wfile.write(str.encode(k + ": " + v))
            self.wfile.write(str.encode('<br/>'))

        # self.wfile.write(str.encode('<br/>'))
        # self.wfile.write(str.encode(datetime.datetime.now().strftime('%Y-%m-%d, %H:%M:%S')))



with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
