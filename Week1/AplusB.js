process.stdin.resume()
process.stdin.setEncoding("ascii")

let input_stdin = ""
let input_stdin_array = ""
let input_currentline = 0

process.stdin.on("data", data => {
  input_stdin += data
})

process.stdin.on("end", () => {
  input_stdin_array = input_stdin.split("\n")
  main()
})

function readLine() {
  return input_stdin_array[input_currentline++]
}

// ///////////// ignore above this line ////////////////////

function main() {
  const n = parseInt(readLine())
  arr = readLine().split(" ")
}
