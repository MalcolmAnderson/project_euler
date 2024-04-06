def find_nth_prime(num_th_prime):
    if num_th_prime < 1:
        return []
    if num_th_prime < 2:
        return [2]
    list_of_primes = [2]
    candidate = 2
    while len(list_of_primes) < num_th_prime:
        candidate += 1
        could_be_prime = True
        for prime in list_of_primes:
            if candidate % prime == 0:
                could_be_prime = False
                break
        if could_be_prime:
            list_of_primes.append(candidate)
            print(f"prime[{len(list_of_primes)}] = {list_of_primes[-1]}")

    return list_of_primes


if __name__ == "__main__":
    NUM_TH_PRIME = 50000
    primes = find_nth_prime(NUM_TH_PRIME)
    print(primes)
    print(primes[-1])
