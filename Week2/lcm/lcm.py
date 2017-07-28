# Uses python3
def lcm(a, b):

    if b == 0:
        return a

    a_prime = a % b
    return lcm(b, a_prime)

if __name__ == "__main__":
    n = input()
    a, b = map(int, n.split())
    print(int((a*b)//(lcm(a, b))))
