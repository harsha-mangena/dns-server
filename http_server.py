import http.server
import socketserver

PORT = 80
DIRECTORY = "/Users/harsha/Work/dns-server/html-files"

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == 'a.com':
            self.path = '/a.html'
        elif self.path == 'b.com':
            self.path = '/b.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def translate_path(self, path):
        # Translate path to the correct directory
        return f"./{DIRECTORY}/{path}"

handler_object = MyHttpRequestHandler
my_server = socketserver.TCPServer(("0.0.0.0", PORT), handler_object)

print(f"Serving HTTP on port {PORT}")
my_server.serve_forever()
