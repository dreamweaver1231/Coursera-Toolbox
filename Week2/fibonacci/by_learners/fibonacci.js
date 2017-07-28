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

//////////////// ignore above this line ////////////////////

function main() {
  const n = parseInt(readLine())
  console.log(fibonacci(n))
}

function fibonacci(num, memo) {
  memo = memo || {}

  if (memo[num]) return memo[num]
  if (num <= 1) return num

  return (memo[num] = fibonacci(num - 1, memo) + fibonacci(num - 2, memo))
}
