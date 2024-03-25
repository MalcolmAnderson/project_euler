if __name__ == "__main__":

    factors = []
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            factors.append(i)
    print(factors)
    total = 0
    for i in factors:
        total += i
    print(total)
