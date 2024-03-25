target = 220
target_factors = [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]

def get_factor_sum(number):
    ret_val = [1]
    for i in range(2, number):
        if number % i == 0 :
            ret_val.append(i)
    return sum(ret_val)

# print(target_factors)
# actual_factors = get_factor_sum(220)
# print(actual_factors)
# print(sum(actual_factors))

def add_factors(main, new):
    for i in new:
        if i not in main:
            main.append(i)
    return main

def find_amicable(number):
    factor_sum = get_factor_sum(number)
    if factor_sum == number:
        return -1
    candidate = get_factor_sum(factor_sum)
    if candidate == number and candidate != 1:
        return factor_sum
    else:
        return -1
    

if __name__ == "__main__":
    # print(get_factor_sum(220))
    # print(get_factor_sum(284))
    # print(find_amicable(220))
    amicables = []
    number_to_be_under = 10000
    for i in range (number_to_be_under):
        if i % 1000 == 0:
            print(i)
        if i not in amicables:
            candidate = find_amicable(i)
            # print(f"{i} {candidate}")
            if candidate != -1:
                amicables.append(i)
                if candidate not in amicables:
                    print(f"Writing {i = } - {candidate = }")
                    amicables.append(candidate)
    print(amicables)
    print(sum(amicables))
    

