// 답은 맞는데 시간 초과 (답만 딱 구하게 하면 초과 안 할 듯)
const readline = require("readline");

const r = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

function getAge(birthDate, nowDate) {
	// 이 함수를 구현해주세요.
	return ''
}


let input = [];

r.on("line", function (line) {
    input.push(line);
    let word = input[0];
    console.log(formatToKoreanNumber(parseInt(word)));


    r.close();
}).on("close", () => {
    process.exit();
});
