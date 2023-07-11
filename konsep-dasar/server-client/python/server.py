from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs


class RequestHandler(BaseHTTPRequestHandler):
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


if __name__ == '__main__':
    port = 8000
    server_address = ('', port)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()
