const readline = require('readline');

process.stdin.setEncoding('utf8');
const rl = readline.createInterface({
  input: process.stdin,
  terminal: false,
});

function readLine(line) {
  if (line !== '\n') {
    console.log(line.toString());
  }
}

rl.on('line', readLine);
