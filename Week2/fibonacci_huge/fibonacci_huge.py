# Uses python3

"""Find the last digit of a sum of the  rst 𝑛 Fibonacci numbers.

Instead of computing this sum in a loop, try to come up with a formula
for 𝐹0 + 𝐹1 + 𝐹2 + ··· + 𝐹𝑛. For this, play with small values of 𝑛.
Then, use a solution for the previous problem.
"""


def get_sequence(mod):
    previous = 0
    current = 1
    arr = [0, 1]

    while True:
        previous, current = current, previous + current
        arr.append(current % mod)
        width = len(arr)

        if(arr[width - 2] == 0 and arr[width - 1] == 1):
            return arr[: -2]


def get_fibonacci_huge_naive(num, mod):
    if num <= 1:
        return num
    seq = get_sequence(mod)
    return seq[num % len(seq)]


if __name__ == '__main__':
    data = input()
    num, mod = map(int, data.split())
    print(get_fibonacci_huge_naive(num, mod))
