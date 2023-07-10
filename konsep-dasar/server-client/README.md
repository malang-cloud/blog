[🏠](../../README.md) / [Konsep Dasar](../README.md)

# Server + Client

Kita sudah tahu bahwa program komputer pada umumnya akan [memproses input dan menghasilkan output](../input-proses-output/README.md). Kita juga sudah mengetahui [bagaimana cara kerja internet](../cara-kerja-internet/README.md).

Pada dasarnya kita bisa membuat sebuah program server yang berjalan terus menerus, menunggu input/request dari client, dan memberikan response untuk setiap request.

## Server

Sebuah program server pada umumnya akan terus berjalan, menunggu input dari client, dan memberikan response (output).

Semisal kita memiliki program Python `server.py` dengan isi sebagai berikut:

```python
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
```

Kita bisa menjalankan program tersebut dengan perintah:

```bash
python server.py
```

Program tersebut akan berjalan di port `8000` dan merespons setiap HTTP request yang diterima melalui port tersebut.

Jika kita membedah program ini lebih lanjut, sebenarnya `httpd.server_forever()` menjalankan perulangan sebagai berikut:

```python
class BaseServer:

    def serve_forever(self, poll_interval=0.5):
        """Handle one request at a time until shutdown.

        Polls for shutdown every poll_interval seconds. Ignores
        self.timeout. If you need to do periodic tasks, do them in
        another thread.
        """
        self.__is_shut_down.clear()
        try:
            # XXX: Consider using another file descriptor or connecting to the
            # socket to wake this up instead of polling. Polling reduces our
            # responsiveness to a shutdown request and wastes cpu at all other
            # times.
            with _ServerSelector() as selector:
                selector.register(self, selectors.EVENT_READ)

                while not self.__shutdown_request:
                    ready = selector.select(poll_interval)
                    # bpo-35017: shutdown() called during select(), exit immediately.
                    if self.__shutdown_request:
                        break
                    if ready:
                        self._handle_request_noblock()

                    self.service_actions()
        finally:
            self.__shutdown_request = False
            self.__is_shut_down.set()
```

Perhatikan bagian `while not self.__shutdown_request:`.

Artinya sebelum ada request untuk mematikan program, maka program akan terus berjalan.

# Port

# Contoh Implementasi

[🏠](../../README.md) / [Konsep Dasar](../README.md)
