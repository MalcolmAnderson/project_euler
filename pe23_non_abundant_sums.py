def get_factors(num):
    ret_val = []
    for i in range(1, num + 1):
        if num % i == 0:
            ret_val.append(i)
    return ret_val


def return_dpa(factors):
    number = factors[-1]
    sum_of_factors = sum(factors) - factors[-1]
    if sum_of_factors > number:
        return "abundant"
    if sum_of_factors < number:
        return "deficient"
    else:
        return "perfect"


if __name__ == "__main__":
    last_usable = 28123
    my_factors = get_factors(28)
    print(my_factors)
    print(return_dpa(my_factors))
    # non_abundant_numbers = []
    abundant_numbers = []
    all_candidates = []
    for i in range(1, last_usable + 1):
        # if i % 1000 == 0:
        #     print(i)
        all_candidates.append(i)
    for i in range(1, last_usable + 1):
        if i % 1000 == 0:
            print(i)
        my_factors = get_factors(i)
        if return_dpa(my_factors) == "abundant":
            abundant_numbers.append(i)
        # if return_dpa(my_factors) != "abundant":
        #     non_abundant_numbers.append(i)
        # else:
        #     abundant_numbers.append(i)
    # print(non_abundant_numbers)
    print(abundant_numbers)

    # print(f"{len(non_abundant_numbers) = }")
    total_abundant = len(abundant_numbers)
    print(f"{total_abundant = }")
    # eliminated = []
    count = 0
    for i in abundant_numbers:
        count += 1
        # print(f"{count = } {i = } {len(all_candidates ) = } {len(eliminated)}")
        print(f"{count = } {i = } {len(all_candidates ) = } {total_abundant = }")
        for j in abundant_numbers:
            if i + j in all_candidates:
                all_candidates.remove(i + j)
            # if i + j not in eliminated:
            #     eliminated.append(i + j)
            #     all_candidates.remove(i + j)
    print(all_candidates)
    print(len(all_candidates))
    print(sum(all_candidates))
