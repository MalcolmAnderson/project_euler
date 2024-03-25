def find_nth_prime(max_prime_value):
    if max_prime_value < 1:
        return []
    if max_prime_value < 4:
        return [2, 3]
    primes = [2, 3]
    candidate = 3
    while candidate < max_prime_value:
        candidate += 2
        could_be_prime = True
        for prime in primes:
            if candidate % prime == 0:
                could_be_prime = False
                break
        if could_be_prime:
            primes.append(candidate)
            print(f"prime[{len(primes)}] = {primes[-1]}")

    return primes



if __name__ == "__main__":
    max_prime_value = 542  # should be 100 primes in this space
    # max_prime_value = 2000000
    primes = find_nth_prime(max_prime_value)
    print(primes)
    total = 0
    for prime in primes:
        total += prime

    print(total)