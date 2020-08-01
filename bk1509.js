// 답은 맞는데 시간 초과 (답만 딱 구하게 하면 초과 안 할 듯)
const readline = require("readline");

const r = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

let input = [];

const is_palindrome = (word) => {
    return word.split("").reverse().join("") === word;
};

const search_palindrome = (word) => {
    if (word.length === 0) return [];
    else if (word.length === 1) return word.split("");
    let answer = [];
    let candidate = [];

    for (let i = 0; i < word.length; i++) {
        let re = new RegExp(word[i], 'g');
        let same_letter_position = [...word.matchAll(re)].map((result) => {
            return result.index
        }).filter((element) => element > i);
        if (same_letter_position.length !== 0) {
            same_letter_position.reverse();
            same_letter_position.map((index) => {
                if (is_palindrome(word.slice(i, index + 1))) {
                    candidate.push([word[i], index - i + 1, i, index]);
                }
            });
        }
    }

    if (candidate.length !== 0) {
        candidate.sort((a, b) => a[1] - b[1]).reverse();
        answer = answer.concat(search_palindrome(word.slice(0, candidate[0][2])));
        answer = answer.concat([word.slice(candidate[0][2], candidate[0][3] + 1)]);
        answer = answer.concat(search_palindrome(word.slice(candidate[0][3] + 1)));
        return answer;
    }

    if (answer.length === 0) {
        return word.split("");
    }


}

r.on("line", function (line) {
    input.push(line);
    let word = input[0];
    console.log(search_palindrome(word).length);

    r.close();
}).on("close", () => {
    process.exit();
});
