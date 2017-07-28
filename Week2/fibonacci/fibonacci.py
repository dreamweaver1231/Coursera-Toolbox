# Uses python3
def calc_fib(n, memo={}):

    if n in memo:
        return memo[n]
    if (n <= 1):
        return n

    memo[n] = calc_fib(n - 1) + calc_fib(n - 2)
    return memo[n]

n = int(input())
print(calc_fib(n))
