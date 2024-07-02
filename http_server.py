import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_PUT(self):
        """Serve a PUT request."""
        path = self.translate_path(self.path)
        
        os.makedirs(os.path.dirname(path), exist_ok=True)

        length = int(self.headers['Content-Length'])
        with open(path, 'wb') as output_file:
            output_file.write(self.rfile.read(length))
        self.send_response(200)
        self.end_headers()

def run(server_class=HTTPServer, handler_class=CustomHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
