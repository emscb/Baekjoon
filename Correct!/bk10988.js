const readline = require("readline");

const r = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

r.on("line", function (word) {
    const isPalindrome = (word) => {
        return word === word.split("").reverse().join("");
    };
    console.log(isPalindrome(word)? 1:0);

    r.close();
}).on("close", () => {
    process.exit();
});
