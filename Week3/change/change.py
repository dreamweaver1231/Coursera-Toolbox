# Uses python3
def get_change(amount):
    coins = [10, 5, 1]
    count = 0

    for coin in coins:
        count += amount // coin
        amount %= coin
    return count


if __name__ == "__main__":
    n = int(input())
    print(get_change(n))
