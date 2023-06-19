[🏠](../README.md)

# Berpikir Kritis dan Komputasional

## Berpikir Kritis

Berpikir kritis adalah kemampuan untuk __menganalisa informasi secara obyektif__. Informasi yang dimaksud bisa berupa fakta, pesan error di layar komputer, atau tren keuntungan perusahaan yang naik/turun.

Sangat disayangkan bahwa pendidikan di Indonesia kerap mematikan bibit-bibit pemikiran kritis yang ada dalam diri para siswa. Kita kerap dilarang mempertanyakan banyak hal. Dipaksa menerima kebenaran absolut yang tidak boleh diragukan. Dan kita cenderung melakukan hal-hal yang sama pada generasi setelah kita.

Untungnya, __pemikiran kritis bisa diasah__ dengan cara yang menyenangkan. Kita perlu membangkitkan kembali rasa ingin tahu yang pernah ada dalam diri kita. Sebuah rasa ingin tahu yang nantinya akan mendorong kita untuk __haus akan pengetahuan__.

Di internet, ada banyak video youtube yang membangkitkan/menjawab rasa ingin tahu, misalnya:

- [Channel alam semenit](https://www.youtube.com/@AlamSemenit)
- [Channel kok bisa](https://www.youtube.com/@KokBisa)
- [Channel veritasium](https://www.youtube.com/results?search_query=veritasium)
- [Channel fireship](https://www.youtube.com/channel/UCsBjURrPoezykLs9EqgamOA)

Dengan terbiasa mempertanyakan "mengapa" dan "bagaimana", maka kita akan __terdorong untuk mempelajari suatu topik lebih jauh__.

Misalnya kita bisa mempertanyakan pertanyaan-pertanyaan berikut:

- Mengapa sih saya harus belajar bahasa pemrograman Python? mengapa tidak pakai bahasa pemrograman PHP saja?
- Mengapa bahasa pemrograman PHP tetap laku, walaupun ada bahasa-bahasa lain yang lebih modern? Apa sih yang spesial dari PHP?
- Mengapa perlu pakai pola MVC? mengapa tidak dijadikan satu file saja?
- Mentapa sih, kok ada kubernetes? Kan bisa kita bikin suatu website dan diunggah ke shared hosting? Apakah itu salah? Kapan kita benar-benar butuh Kubernetes?
- Mengapa sih, kok ada error "missing semicolon"? Kalau komputer tahu bahwa kita kurang titik koma, mengapa tidak otomatis ditambahkan saja? Mengapa harus melempar error?

Dari pertanyaan-pertanyaan di atas, kita bisa coba cari alasannya. Kita bia buka diskusi di stack overflow, memancing pertanyaan di twitter, membiarkan pendapat kita disanggah orang lain.

Berpikir kritis akan memberikan kita bahan bakar untuk terus mengejar pengetahuan. Berpikir kritis juga bisa membantu kita menemukan akar permasalahan secara lebih mendalam. Apakah benar, kita harus menulis kode kita dari awal? Sebenarnya bagian mana dari kode kita yang bermasalah? Atau lebih jauh lagi, apakah masalah saya hanya bisa diselesaikan dengan membuat fitur baru? Apakah benar, masalah yang saat ini dihadapi tidak bisa diselesaikan dengan fitur yang ada sekarang? Apakah benar, penambahan fitur katalog akan meningkatkan penjualan? Bagaimana saya bisa menguji hipotesa itu?

## Berpikir Komputasional

Berpikir komputasional adalah cara untuk __memformulasikan masalah__, dan __membuat tahapan-tahapan solusi__.

Pada dasarnya, setiap manusia bisa berpikir. Namun demikian, kemampuan berpikir komputasional merupakah sesuatu yang harus dilatih dan dipelajari. __Setiap programmer, pasti memiliki kemampuan ini__. Programmer yang lebih senior bisa memecahkan masalah-masalah yang lebih abstrak dan rumit.

Mari kita lihat contoh sebuah masalah yang cukup abstrak.

```
Bagaimana supaya cepat kaya?
```

Nah, ini contoh permasalahan umum yang menarik untuk diselesaikan secara komputasional.

### Memperjelas Masalah

Langkah pertama yang perlu kita lakukan adalah memperjelas dulu, apa itu definisi `kaya`.

Salah satu definisi `kaya` yang menurut saya cukup masuk akal adalah: `banyaknya waktu yang bisa kita habiskan dengan bergaya hidup normal, tanpa bekerja`.

Jadi sekarang kita geser definisi `kaya` yang abstrak ke definisi waktu. Mari kita mulai menghitung.

- Sebulan, saya menghabiskan uang 2 juta rupiah.
- Berarti dalam setahun, saya menghabiskan uang 24 juta rupiah.
- Tabungan saya sekarang 6 juta rupiah
- Berarti kekayaan saya adalah tiga bulan. Saya bisa bermalas-malasan 3 bulan dan tetap hidup sebelum tabungan saya habis, dan saya jatuh miskin.
- Saya akan merasa kaya kalau saya bisa tidak bekerja selama dua tahun dan baik-baik saja
- Eits, tunggu dulu. Tidak semudah itu, kita punya laju inflasi 2-4% dalam setahun (sumber: [artikel Bank Indonesia](https://www.bi.go.id/en/publikasi/ruang-media/news-release/Pages/sp_2432222.aspx))

Nah, setidaknya target kita sudah lebih jelas sekarang.

- Saya harus tetap menghasilkan `24 juta` dalam setahun supaya saya bisa tetap hidup.
- Saya harus menghasilkan `24 juta x 104%` supaya saya bisa hidup bebas di tahun berikutnya.
- Saya harus menghasilkan `24 juta x 104 % x 104%` supaya saya bisa hidup bebas di tahun kedua selanjutnya.
- Jadi jika tahun ini saya bisa menghasilkan `74.92 juta`, bagaimanapun caranya, maka saya kaya.

Bagi angka ini dengan 12, maka kita dapat `6.243 juta`.

Ya sudah, cari pekerjaan/usaha yang bisa memberi saya `6.5 juta` per bulan.

### Menetapkan Solusi

Kita baru saja menyelesaikan langkah pertama dengan mengubah kata `kaya` menjadi sesuatu yang lebih bisa disepakati bersama: `6.5 juta per bulan`.

Berikutnya kita akan coba bagaimana mencari solusinya. Kemampuan berpikir kritis akan membantu kita untuk bisa menemukan solusi-solusi yang efektif (tingkat keberhasilannya tinggi) dan efisien (usahanya rendah). Beberapa solusi yang mungkin terpikir:

- Membeli obligasi: Ini setidaknya bisa menahan laju inflasi. Beberapa obligasi bisa dicairkan lebih mudah daripada deposito.
- Menurunkan pengeluaran. Dari uang 2 juta yang kita keluarkan sebulan tadi, adakah yang bisa dihemat tanpa banyak mengurangi kenyamanan? Mungkin kita bisa merebus air daripada beli air mineral galonan? Kalau bisa, ini bisa mengecilkan target kita.
- Memperbesar pendapatan:
    - Ambil job intern yang dibayar
    - Mendaftar jadi mitra ojol, sehingga bisa dapat penghasilan di luar jam kuliah
    - Menerima les komputer
    - Dsb.
- Coba hitung, apakah rencana yang sudah kita buat bisa membuat kita kaya. Jika belum, coba pikirkan lagi, atau tanya pada mereka yang lebih jago masalah keuangan.

# Tentang Artikel ini

- Penulis: Go Frendi Gunawan
- Ditulis pada: 16 Juni 2023
- Penyunting: Go Frendi Gunawan
- Terakhir disunting pada: 19 Juni 2023

[🏠](../README.md)