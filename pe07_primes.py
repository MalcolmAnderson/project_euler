



def find_nth_prime(num_th_prime):
    if num_th_prime < 1:
        return []
    if num_th_prime < 2:
        return [2]
    primes = [2]
    candidate = 2
    while len(primes) < num_th_prime:
        candidate += 1
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
    num_th_prime = 10001
    primes = find_nth_prime(num_th_prime)
    print(primes)
    print(primes[-1])