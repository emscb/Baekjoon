const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

// rl.prompt("## ");

rl.on("line", function (line) {
    let num = parseInt(line);
    let ans = 0;

    if (num < 100) {
        ans = num;
        console.log(ans)
    } else {
        for (let i = 100; i < num + 1; i++) {
            let lt = [];
            for (let k = 0; k < 3; k++) {
                lt.push(i.toString()[k]);
            }
            if ((lt[2] - lt[1]) === (lt[1] - lt[0])) {
                ans += 1
            }
        }
        console.log(ans + 99);
    }
    rl.close();
}).on("close", function () {
    process.exit();
});

