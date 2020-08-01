const readline = require("readline");

const r = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

let input = [];

r.on("line", function (line) {
    input.push(line);
    let word = input[0];
    let answer = '';
    for (let i = 0; i < word.length; i++) {
        if (word[i] === "A") {
            answer += "X";
        } else if (word[i] === "B") {
            answer += "Y";
        } else if (word[i] === "C") {
            answer += "Z";
        } else {
            answer += String.fromCharCode(word[i].charCodeAt() - 3);
        }
    }
    console.log(answer);

    r.close();
}).on("close", () => {
    process.exit();
});
