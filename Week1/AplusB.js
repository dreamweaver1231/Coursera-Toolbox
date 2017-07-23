var readline = require("readline")

process.stdin.setEncoding("utf8")
var rl = readline.createInterface({
  input: process.stdin,
  terminal: false,
})

rl.on("line", readLine)

function readLine(line) {
  console.log(parseInt(line.toString()))
  if (line !== "\n") {
    console.log(line.toString())
  }
}
