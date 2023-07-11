[🏠](../../README.md) / [Konsep Dasar](../README.md)

# Server + Client

Kita sudah tahu bahwa program komputer pada umumnya akan [memproses input dan menghasilkan output](../input-proses-output/README.md). Kita juga sudah mengetahui [bagaimana cara kerja internet](../cara-kerja-internet/README.md).

Pada dasarnya kita bisa membuat sebuah program server yang berjalan terus menerus, menunggu input/request dari client, dan memberikan response untuk setiap request.

## Server

Sebuah program server pada umumnya akan terus berjalan, menunggu input dari client, dan memberikan response (output).

Sebuah program server juga umumnya bisa melayani lebih dari satu client. Misalnya, sebuah web server bisa diakses dari banyak device oleh banyak user.

Mari kita lihat contoh sebuah aplikasi server yang ditulis dengan menggunakan bahasa Python. Semisal kita memiliki sebuah program Python `server.py` dengan isi sebagai berikut:

```python
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

```

Kita bisa menjalankan program tersebut dengan perintah:

```bash
python server.py
```

Program tersebut akan berjalan di komputer kalian, menerima setiap HTTP request di port `8000` dan memberikan response sesuai isi program.

Response yang diberikan kurang lebih sebagai berikut:

- Jika user mengakses url `/?name=<sebuah-nama>`, maka program akan memberikan response `Hello, <sebuah-nama>!`
- Jika user mengakses url `/`, maka program akan memberikan response `Hello, world!`
- Jika user mengakses url lain selain `/`, maka program akan memberikan reponse dengan status `404`.

Jika kita membedah program ini lebih lanjut, kita akan menjumpai sebuah perulangan di dalam `httpd.server_forever()`.

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

Dalam method `server_forever`, terdapat sebuah perulangan dengan kondisi `not self.__shutdown_request`.  Artinya sebelum ada request untuk mematikan program, maka program akan terus berjalan.

## Client

Di bagian sebelumnya, kita sudah melihat bagaimana menjalankan sebuah server.

Selanjutnya kita bisa menjalankan aplikasi HTTP client. Ada beberapa aplikasi HTTP client yang bisa kita gunakan:

- Web browser (Firefox, Chrome, Opera, atau Microsoft edge)
- [Postman](https://www.postman.com/product/rest-client/)
- Curl

Cara paling mudah utuk mengirimkan request ke aplikasi server yang sudah kita jalankan, maka kita bisa membuka browser dan mengetikkan alamat berikut di address bar: `http://localhost:8000?name=Budi`.

Jika kalian terbiasa dengan Curl, kalian juga bisa membuka terminal dan menjalankan perintah berikut:

```bash
curl localhost:8000\?name=budi
```

Ada beberapa hal yang perlu diperhatikan di sini:

- `localhost` adalah nama host untuk komputer lokal kita.
- Alamat `localhost`, akan diterjemahkan menjadi IP `127.0.0.1` yang juga merujuk pada komputer lokal kita.
- `8000` adalah port di mana aplikasi server kita akan mendengarkan request dan mengirimkan balasan
- Karena aplikasi server kita berjalan di komputer lokal, maka kita bisa mengakses nya dengan alamat `localhost:8000` atau `127.0.0.1:8000`.
- `http` adalah protocol yang digunakan untuk komunikasi antara client/server dalam kasus ini.
- Ada beberapa protocol lain seperti `ftp`, `smtp`, dan sebagainya.
- Protocol adalah cara komunikasi yang disepakati oleh server dan client. Kita bisa membuat protocol sendiri, atau membuat sebuah protocol di atas di atas protocol lain. Misal protocol `http` berjalan di atas protocol `tcp/ip`.

# Contoh Implementasi

- [Python](python/server.py)


# Tentang Artikel ini

- Penulis: Go Frendi Gunawan
- Ditulis pada: 11 Juli 2023
- Penyunting: Go Frendi Gunawan
- Terakhir disunting pada: 11 Juli 2023


[🏠](../../README.md) / [Konsep Dasar](../README.md)
