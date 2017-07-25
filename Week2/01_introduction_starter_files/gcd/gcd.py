# Uses python3
def gcd_naive(a, b):

    if b == 0:
        return a

    a_prime = a % b
    return gcd_naive(b, a_prime)

if __name__ == "__main__":
    n = input()
    a, b = map(int, n.split())
    print(gcd_naive(a, b))
