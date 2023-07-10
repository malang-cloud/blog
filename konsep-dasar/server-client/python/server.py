from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        base_path = parsed_url.path
        if base_path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            query_params = parse_qs(parsed_url.query)
            name = query_params.get('name', ['world'])[0]
            message = f'Hello, {name}!'
            self.wfile.write(message.encode())
        else:
            self.send_response(404)
            self.end_headers()


def run(server_class, handler_class, port):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()


if __name__ == '__main__':
    run(HTTPServer, MyHandler, 8000)
