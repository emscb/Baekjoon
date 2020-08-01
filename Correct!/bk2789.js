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
    let del_list = "CAMBRIDGE".split("");
    for (let i = 0; i < word.length; i++) {
        if (!del_list.includes(word[i])) {
            answer += word[i];
        }
    }
    console.log(answer);

    r.close();
}).on("close", () => {
    process.exit();
});
