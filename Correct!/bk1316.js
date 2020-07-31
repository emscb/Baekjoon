const readline = require("readline");

const r = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

let input = [];

r.on("line", function (word) {
    input.push(word);
}).on("close", () => {
    let answer = 0;
    for (let i = 1; i < input.length; i++) {
        let word = input[i];
        let letters = [];
        let is_false = false;
        for (let w = 0; w < word.length; w++) {
            if (letters.includes(word[w]) && word[w] !== letters.slice(letters.length - 1)[0]) {
                is_false = true;
                break
            } else {
                letters.push(word[w]);
            }
        }
        if (!is_false) {
            answer += 1;
        }
    }
    console.log(answer);

    process.exit();
});
