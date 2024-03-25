 # 2520 is the smallest number that can be divided by each of the numbers from 
# to without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the 
# numbers from 1 to 20 ?

def get_primes(number):
    if number < 2:
        return []
    
    if number < 3:
        return [2]
    
    primes = [2]

    for i in range(3, number+1):
        is_prime = True
        for prime in primes:
            if i % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)

    return primes

def gcd(a, b):
    if(b==0):
        return a
    # a_mod_b = a%b
    return gcd(b, a%b)


def lcm(n):
    ans = 1
    for i in range(1, n + 1):
        # greatest_common_denomenator = gcd(ans, i)
        # answer_times_i = ans * i
        # a_div_b = answer_times_i / greatest_common_denomenator
        ans = (ans * i) // gcd(ans, i)
        # ans = int((answer_times_i)/greatest_common_denomenator)        
    return ans
   



if __name__ == "__main__":
    # print(gcd(5, 15))
    # print(gcd(15, 5))
    # print(gcd(3, 7))
    # print(gcd(7, 3))




    print(lcm(20))

    # number = 10
    # numbers = list(range(number - 1, 1, -1))
    # total = number
    # for num in numbers:
    #     print(f"{total = } {num = } {total % num = }")
    #     if total % num != 0:
    #         total *= num


    # total = 1
    # for prime in primes:
    #     total *= prime
    # print(f"{primes = }")
    # print(f"{total = }")