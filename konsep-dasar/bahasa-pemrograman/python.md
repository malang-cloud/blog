[🏠](../../README.md) / [Konsep Dasar](../README.md) / [Bahasa Pemrograman](README.md)

# Menginstall Python

Sebelumnya pastikan kalian sudah tahu penggunaan [CLI](../cli.md).

Untuk menginstall Python, kita bisa mengunjungi [website resmi Python](https://www.python.org/downloads/).

# Menginstall beberapa versi Python

Untuk menginstall beberapa versi python yang berbeda di komputer yang sama, kita bisa menggunakan `pyenv`.

Silahkan klik [link berikut](https://github.com/pyenv/pyenv#installation) untuk memulai instalasi pyenv.

Pastikan juga kalian sudah memiliki software-software yang dibutuhkan untuk menginstall pyenv. Jika instalasi kalian bermasalah, silahkan ikuti langkah [berikut](https://github.com/pyenv/pyenv/wiki#suggested-build-environment).

# Mengkonfirmasi instalasi Python

Untuk mengkonfirmasi instalasi Python, kalian bisa menjalankan perintah berikut di terminal:

```bash
python --version
```

Seharusnya akan muncul versi Python yang kalian pakai.

# Menjalankan aplikasi Python

Untuk menjalankan sebuah script Python, kita bisa menjalankan perintah berikut melalui terminal:

```bash
python nama-script.py
```

Misal, kita memiliki sebuah script sederhana `hello.py` sebagai berikut:

```python
print('hello world')
```

Maka untuk menjalankannya, kita cukup mengetikkan perintah `python hello.py`.

# Menggunakan package manager

Dalam menulis sebuah script Python kadang kita membutuhkan kode-kode yang sebelumnya telah pernah ditulis oleh programmer lain.

Kita bisa mengunjungi [pypy.org](https://pypi.org/) untuk melihat daftar package yang sudah di publish dan siap kita pakai.

Beberapa package yang sering dipakai misalnya:
- [Numpy](https://pypi.org/project/numpy/)
- [Pandas](https://pypi.org/project/pandas/)
- [FastAPI](https://pypi.org/project/fastapi/)
- [IPython](https://pypi.org/project/ipython/)
- dan sebagainya

Untuk menginstall package yang dibutuhkan, kita harus terlebih dahulu [menginstall pip](https://pip.pypa.io/en/stable/installation/). Setelah pip terinstall, kita bisa menjalankan perintah berikut di terminal:

```bash
pip install <nama-package>
# atau
pip install <nama-package>==<versi-package>
```

Semisal kita ingin menginstall IPython, sebuah package yang membantu kita untuk menjalankan mode interaktif secara lebih mudah, maka kita bisa menjalankan `pip install ipython`.

# Mengimpor package

Kita bisa menggunakan package yang sudah kita install menggunakan pip dengan menggunakan keyword `import`.

Semisal kita sudah menginstall package `jsons` menggunakan perintah `pip install jsons`.

Seandainya kita ingin memanggil fungsi dumps yang ada di package `jsons`, maka kita bisa menggunakan keyword `import`:

```python
import jsons

orang = jsons.loads('{"nama": "budi", "umur": 20}') # mengubah string json menjadi python dictionary
print(orang["nama"])
```

# REPL (Read Eval Print Loop)

Beberapa bahasa pemrograman seperti Python, JavaScript, dan PHP memiliki fitur2 REPL sehingga kita bisa menjalankan kode program secara interaktif.

Untuk memasuki mode REPL di python, kita bisa mengetikkan perintah `python` di terminal tanpa parameter apapun:

```
python
```

Setelah memasuki mode interaktif, kita bisa mengetikkan kode-kode Python yang akan di-evaluasi dan dijalankan. Untuk keluar dari mode interaktif ini, kita mengetikkan perintah `exit()`

```
Python 3.9.10 (main, May  5 2023, 04:44:25) 
[GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 3 + 4
7
>>> exit()
```

Kalau kalian sudah menginstall package ipython, kalian bsia mengetikkan `ipython` untuk memasuki mode interaktif yang lebih kaya fitur. Misalnya kalian bisa menekan tombol `tab` untuk auto completion.


[🏠](../../README.md) / [Konsep Dasar](../README.md) / [Bahasa Pemrograman](README.md)