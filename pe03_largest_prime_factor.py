def prime_factor(number):
    keep_going = True
    count = 0 # count is stored in primes[0]
    primes = [0]
    candidate = 2
    while keep_going:
        count += 1
        if number % candidate == 0:
            number = number // candidate
            primes.append(candidate)
            if number == 1:
                keep_going = False
        else:
            candidate += 1
    primes[0] = count
    return primes


    return [0]

if __name__ == "__main__":
    my_number = 600851475143
    # my_number = 13195
    # my_number = 15
    print(f"{my_number = }")
    primes = prime_factor(my_number)
    print (f"{primes=}")
    print(f"{primes[-1]}")

    # assert primes[-1] == 29