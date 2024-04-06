def get_triangle_numbers_up_to(number):
    triangle_numbers = []
    for i in range(1, number + 1):
        if i % 1000 == 0:
            print(i)
        total = 0
        for j in range(i + 1):
            total += j
        triangle_numbers.append(total)
    return triangle_numbers


def get_factors(number):
    if number == 1:
        return [1]
    list_of_factors = []
    int_half_the_number_plus_one = number // 2 + 1
    count = 0
    for i in range(1, int_half_the_number_plus_one):
        count += 1
        if i not in (list_of_factors) and number % i == 0:
            list_of_factors.append(i)
            other_number = number // i
            if other_number not in (list_of_factors):
                list_of_factors.append(other_number)
    list_of_factors.sort()
    list_of_factors[0] = count
    return list_of_factors


def get_factors_2(number):
    if number == 1:
        return [1]
    list_of_factors = []
    current_number = 1
    max_number = number
    count = 0
    while current_number < max_number:
        count += 1
        if current_number not in (list_of_factors) and number % current_number == 0:
            list_of_factors.append(current_number)
            other_number = number // current_number
            if other_number not in (list_of_factors):
                list_of_factors.append(other_number)
            max_number = number // current_number
        current_number += 1
    list_of_factors.sort()
    list_of_factors[0] = count
    return list_of_factors


def print_status(max_factor_count, nth_triange_number, factor_count, current_triange_number):
    print(f"{max_factor_count = } {nth_triange_number = } {factor_count} {current_triange_number = }")


if __name__ == "__main__":
    if True:
        factor_count = 0
        max_factor_count = 0
        nth_triange_number = 0
        current_triange_number = 0
        while factor_count < 501:
            nth_triange_number += 1
            current_triange_number += nth_triange_number
            factors = get_factors_2(current_triange_number)
            factor_count = len(factors) - 1
            if factor_count > max_factor_count:
                max_factor_count = factor_count
                print_status(max_factor_count, nth_triange_number, factor_count, current_triange_number)
            # print(f"{factor_count = } {nth_triange_number = } {current_triange_number = } {factors = }")
            if nth_triange_number % 100 == 0:
                print_status(max_factor_count, nth_triange_number, factor_count, current_triange_number)
        print("...")
        print_status(max_factor_count, nth_triange_number, factor_count, current_triange_number)
    else:
        test_number = 289978899
        fast_run_factors = get_factors_2(test_number)
        slow_run_factors = get_factors(test_number)
        fast_run = fast_run_factors[0]
        slow_run = slow_run_factors[0]
        print(
            f"{len(fast_run_factors)} {len(slow_run_factors)} {fast_run = } {slow_run = } fast / slow = {fast_run / slow_run * 100}"
        )

    # triangles = get_triangle_numbers_up_to(7)
    # print(triangles)
