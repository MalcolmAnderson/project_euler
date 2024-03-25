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

def get_prime_factors(number, primes):
    factors = []
    prime_count = 0
    while number > 1:
        # print(f"{primes[prime_count] = } remainder = {number % primes[prime_count]}")
        if number % primes[prime_count] == 0:
            factors.append(primes[prime_count])
            while number % primes[prime_count] == 0: # handles multiple multiples like 28 and 4
                number //= primes[prime_count]
        prime_count += 1 # only one prime per
    return factors
        
        
def get_triangle_numbers_up_to(number):
    numbers = []
    for i in range(1, number + 1):
        print(i)
        total = 0
        for j in range( i + 1):
            total += j
        numbers.append(total)
    return numbers




if __name__ == "__main__":
    num_th_prime = 50000
    primes = find_nth_prime(num_th_prime)
    print(primes)
    print(primes[-1])

    triangles = get_triangle_numbers_up_to(200000)
    print(triangles)

    max_factors = 0
    for num in triangles:
        print(f"{num = }")
        factors = get_prime_factors(num, primes)
        print(factors)
        if len(factors) > max_factors:
            max_factors = len(factors)
        print(f"{num = } {len(factors) = } max_factors = {max_factors}")
        trigger = len(factors) > 500
        if trigger:
            quit()

    # factors = get_prime_factors(6409990, primes)
