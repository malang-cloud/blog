[🏠](../README.md) / [Konsep Dasar](./README.md)

# Command Line Interface

Untuk bisa berkomunikasi dengan komputer, kita membutuhkan sebuah antarmuka (interface).

Secara umum ada dua macam antarmuka:

- GUI (Graphical User Interface): Antarmuka yang sering kita pakai sehari-hari baik di ponsel ataupun di komputer. Antarmuka ini biasanya memungkinkan kita untuk melakukan klik/tap pada pada icon atau menu aplikasi.
- TUI (Text User Interface): Antarmuka yang hanya berupa text saja. Kalian mungkin mengenal antarmuka ini dari adegan hacking di film-film Hollywood.

Command Line Interface adalah sebuah antarmuka yang memungkinkan kita menuliskan perintah-perintah teks pada komputer, dan melihat hasilnya secara interaktif, baris per-baris.

CLI biasa digunakan dalam TUI, tapi bisa juga dipakai pada mode grafis (GUI).

Jika kalian menggunakan operating system Windows/Mac/Linux, dan menggunakan tampilan GUI, maka kalian biasanya akan menemukan program `shell` atau `terminal`. Dari sana, kalian akan bisa menggunakan CLI.

Perintah-perintah yang bisa kalian gunakan pada CLI akan sangat tergantung pada dua hal:
- Operating system yang kalian pakai.
    - Mac/Linux memiliki perintah yang mirip.
    - Windows memiliki perintah yang berbeda, namun ada juga beberapa perintah Mac/Linux yang bisa berjalan di Windows berkat PowerShell.
- Shell yang kalian pakai. Saat ini shell yang paling umum dipakai adalah `bash`.

Jika kalian menggunakan Windows, maka sebaiknya menginstall WSL2 juga, karena nantinya kalian akan sering berurusan dengan CLI untuk development/akses server. Kebanyakan aplikasi CLI untuk development/akses server memiliki kompatibilitas yang tinggi dengan UNIX/Linux. Untuk menginstall WSL, ikuti [panduan berikut](https://learn.microsoft.com/en-us/windows/wsl/install). Usahakan untuk memilih distro linux yang populer seperti `ubuntu`, supaya kalian lebih mudah menemukan bantuan jika ada masalah.

Jika kalian menggunakan Mac, maka sebaiknya menginstall homebrew. Untuk menginstall homebrew, ikuti [panduan berikut](https://brew.sh/).

# Mengapa CLI?

Ada beberapa alasan mengapa banyak programmer menyukai CLI:

- Kebanyakan software untuk development berjalan di CLI
- Perintah CLI bisa diulang dengan mudah (tinggal copy paste dan jalankan di terminal), berbeda dengan aplikasi GUI yang mengahruskan kita untuk menekan tombol/icon secara berurutan.
- Karena perintah CLI mudah diulang, maka mudah pula di otomasi, misalnya dengan menggunakan [shell script](https://www.shellscript.sh/).

Biasanya banyak pemula yang tidak nyaman dengan CLI. Tapi jangan khawatir, kalian tidak harus meninggalkan GUI untuk menjalankan perintah-perintah CLI. Lagipula, perintah-perintah CLI dasar mudah dipelajari. Kalian akan terbiasa hanya dalam beberapa menit.

# Menggunakan CLI

Kalian bisa membuka CLI dengan menjalankan terminal di komputer kalian. Jika kalian menggunakan WSL, maka kalian perlu mengetikkan perintah `wsl` disusul dengan tombol `enter`.

Diharapkan kalian menggunakan shell `bash` atau `zsh`. Jika kalian menggunakan Linux, Mac, atau WSL, maka secara otomatis komputer kalian akan menggunakan salah satu dari kedua shell tersebut.

Menggunakan CLI sebenarnya mirip dengan menggunakan aplikasi chatting. Kalian menuliskan sesuatu, dan komputer memberikan balasan. Hanya saja, perintah-perintah yang bisa dikenali komputer akan sangat terbatas. Kalian perlu belajar menyampaikan keinginan kalian dalam perintah-perintah sederhana tadi.

Mari kita coba beberapa perintah yang sering dipakai.

## pwd

Kalian bisa menggunakan perintah ini untuk mengetahui di direktori/folder kalian bekerja saat ini.

```bash
pwd
```

Komputer akan menampilkan lokasi direktori tempat kalian berada sekarang (working directory)

```
/home/gofrendi
```

## ls

Kalian bisa menggunakan perintah ini untuk melihat isi dari sebuah direktori.

```bash
ls
```

Komputer akan menampilka isi dari direktori kalian.

```
Downloads  Documents
```

Kalian juga bisa menampilkan isi dari direktori yang lain:

```bash
ls /usr/bin
```

Atau kalian juga bisa menambahkan opsi untuk menampilkan isi direktori secara berbeda:

```bash
ls /usr/bin -l
```

Kalian juga bisa mengetikkan `ls --help` untuk mendapatkan panduan lengkap menggunakan perintah `ls`.

# cd

Selanjutnya, perintah yang juga kerap digunakan adalah `cd`. Perintah ini memungkinkan kalian untuk berpindah working directory.

```bash
cd /usr/bin
ls
```

Kalian juga bisa menggunakan `cd ..` untuk berpindah satu direktori di atas current working directory:

```bash
pwd
cd ..
pwd
```

Ada beberapa aturan khusus saat kalian ingin menyebutkan nama direktori:

- Awalan `/` menandakan alamat mutlak.
    - Jika kalian mengawali alamat direktori dengan `/`, maka komputer akan menganggap ini sebagai alamat mutlak
    - Jika kalian tidak mengawali alamat direktori dengan `/`, maka komputer akan menganggap alamat direktori kalian relatif terhadap current working direktori. Misal
        - Saat ini kalian berada di direktori `/home`
        - Maka saat kalian menuliskan `cd gofrendi`, artinya kalian ingin berpindah ke direktori `/home/gofrendi`
        - Tapi jika kalian menuliskan `cd /usr/bin`, maka artinya kalian benar-benar ingin berpindah ke direktori `/usr/bin` tanpa peduli di mana lokasi kalian sekarang
- Awalan `~` menandakan home direktori, misal:
    - Saat ini kalian berada di direktori `/usr/bin`
    - Maka saat kalian mengetikkan `cd ~`, artinya kalian ingin berpindah ke home directory kalian.
    - Home directory di linux atau mac biasanya adalah `/home/nama-pengguna`. Misalnya home directory saya adalah `/home/gofrendi`.
- Awalan `..` menandakan berpindah ke satu folder di atas current directory (disebut juga parent directory)

## cat

Perintah lain yang kerap dipakai adalah `cat`. Perintah ini berguna untuk menampilkan isi dari sebuah file.

```bash
cat ~/.zshrc
```

## clear

Perintah ini berguna untuk membersihkan tampilan terminal

```bash
clear
```

# Beberapa tips

- Kalian bisa menekan `panah atas` untuk menampilkan perintah sebelumnya. Kalian juga bisa menekan panah atas beberapa kali jika dibutuhkan.
- Kalian bisa menekan tombol `tab` untuk melengkapi perintah yang kalian tulis secara otomatis.

# Lebih lanjut

Kita baru saja membahas perintah-perintah CLI yang umum dipakai. Untuk mempelajari CLI lebih lanjut, kalian bisa mengunjungi [artikel di freecodecamp tentang CLI](https://www.freecodecamp.org/news/command-line-for-beginners/).

[🏠](../README.md) / [Konsep Dasar](./README.md)
