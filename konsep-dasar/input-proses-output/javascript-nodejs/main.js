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