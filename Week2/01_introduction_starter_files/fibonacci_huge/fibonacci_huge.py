# Uses python3

def get_sequence():
    previous = 0
    current = 1
    arr = [0, 1]

    while True:
        previous, current = current, previous + current

        arr.append(current % m)
        width = len(arr)
        if(arr[width - 2] == 0 and arr[width - 1] == 1):
            return arr[: -2]

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n
    seq = get_sequence(m)
    return seq[n % len(seq)]

if __name__ == '__main__':
    data = input()
    n, m = map(int, data.split())
    print(get_fibonacci_huge_naive(n, m))
