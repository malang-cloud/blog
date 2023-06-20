[🏠](../../README.md) / [Konsep Dasar](../README.md)

# Input + Proses = Output

Komputer adalah sebuah mesin, dan pada umumnya sebuah mesin akan menerima input, melakukan pemrosesan dan mengeluarkan output.

Contohnya mesin pada motor/mobil. Inputnya berupa bahan bakar, prosesnya berupa pembakaran, dan output nya berupa gerakan piston untuk memutar roda.

Komputer generasi awal tersusun atas banyak perangkat keras (hardware) yang bisa mengubah sinyal input menjadi sinyal output. Komputer ini bisa melakukan operasi-operasi aritmetika seperti penjumlahan, pengurangan, dan sebagainya.

Pada tahapan lebih lanjut, orang-orang mulai mengembangkan perangkat lunak (software). Dibandingkan perangkat keras (hardware), perangkat lunak lebih mudah dikembangkan dan dimodifikasi. Jadi kita bisa mendefinisikan proses-proses baru tanpa perlu mengubah perangkat keras di komputer keras.

Dewasa ini, pekerjaan rekayasa perangkat lunak menjadi sangat populer. Orang-orang yang merekayasa/membuat perangkat lunak kita kenal dengan sebutan programmer.

Kita bisa menulis perangkat lunak menggunakan bahasa pemrograman. Kita akan membahas lebih dalam tentang karakteristik dari setiap bahasa pemrograman [di artikel yang berbeda](bahasa-pemrograman.md).

Untuk saat ini, kita akan mencoba untuk melihat contoh aplikasi untuk menerima input, melakukan proses, dan menampilkan output dalam beberapa bahasa pemrograman yang tampaknya cukup populer.

Skenario yang akan digunakan cukup mudah, yakni:
- Mengambil 2 input, `a` dan `b`
- Melakukan proses penjumlahan `c = a + b`
- Menampilkan output `c`

# Python

```python
# input
input_a = input('Nilai A: ')
input_b = input('Nilai B: ')

# proses
a = int(input_a)
b = int(input_b)
c = a + b

# output
print(f'Nilai A + B = {c}')
```

Untuk pembahasan lebih lanjut silahkan klik [link berikut](./python/README.md).

# JavaScript (di browser)

```html
<script type="text/javascript">
// input
const input_a = window.prompt('Nilai A: ');
const input_b = window.prompt('Nilai B: ');

// proses
const a = parseInt(input_a);
const b = parseInt(input_b);
const c = a + b;

// output
window.alert(`Nilai A + B = ${c}`);

</script>
```

Untuk pembahasan lebih lanjut silahkan klik [link berikut](./javascript-browser/README.md).

# JavaScript (menggunakan Node.Js)

```javascript
// import module "readline"
const readline = require('readline');

// membuat instance dari antarmuka "readline"
const rl = readline.createInterface({
    input: process.stdin, // Membaca dari CLI
    output: process.stdout // menulis ke CLI
});

const prompt = (prompt) => {
    return new Promise((resolve) => {
        rl.question(prompt, (answer) => {
            resolve(answer);
        });
    });
};

(async() => {
    // input
    const input_a = await prompt('Nilai A: ');
    const input_b = await prompt('Nilai B: ');

    // proses
    const a = parseInt(input_a);
    const b = parseInt(input_b);
    const c = a + b;

    // output
    console.log(`Nilai A + B = ${c}`);
    rl.close();
})();

rl.on('close', () => process.exit(0));
```

Untuk pembahasan lebih lanjut silahkan klik [link berikut](./javascript-nodejs/README.md).

# PHP

```php
<?php

$inputA = readline('Nilai A: ');
$inputB = readline('Nilai B: ');

$a = intval($inputA);
$b = intval($inputB);
$c = $a + $b;

echo "Nilai A + B = $c\n";
```

Untuk pembahasan lebih lanjut silahkan klik [link berikut](./php/README.md).


# Java

```java
import java.util.Scanner;

public class UserInputExample {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Nilai A: ");
        int a = scanner.nextInt();

        System.out.print("Nilai B: ");
        int b = scanner.nextInt();

        int c = a + b;

        System.out.println("Nilai A + B = " + c);

        scanner.close();
    }
}
```

Untuk pembahasan lebih lanjut silahkan klik [link berikut](./java/README.md).

# Golang

```go
package main

import (
	"fmt"
	"os"
)

func main() {
	var a, b int

	fmt.Print("Nilai A: ")
	fmt.Scanln(&a)

	fmt.Print("Nilai B: ")
	fmt.Scanln(&b)

	c := a + b

	fmt.Printf("Nilai A + B = %d\n", c)

	os.Exit(0)
}
```


Untuk pembahasan lebih lanjut silahkan klik [link berikut](./go/README.md).

# C

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int a, b;

    printf("Nilai A: ");
    scanf("%d", &a);

    printf("Nilai B: ");
    scanf("%d", &b);

    int c = a + b;

    printf("Nilai A + B = %d\n", c);

    return 0;
}
```

Untuk pembahasan lebih lanjut silahkan klik [link berikut](./c/README.md).


[🏠](../../README.md) / [Konsep Dasar](../README.md)