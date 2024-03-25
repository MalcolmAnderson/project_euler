def if_even(number):
    return number // 2

def if_odd(number):
    return 3 * number + 1

def is_even(number):
    return number % 2 == 0

if __name__ == "__main__":
    num_to_get_to = 1000000
    max_sequence_len = 0
    max_sequence = []
    for i in range(1, num_to_get_to):
        print(i)
        number = i
        list_of_values = [i]
        while number != 1:
            # number = if_even(number) if is_even(number) else if_odd(number)
            if is_even(number):
                number = if_even(number)
            else:
                number = if_odd(number)
            list_of_values.append(number)
        if len(list_of_values) > max_sequence_len:
            max_sequence_len = len(list_of_values)
            max_sequence = list_of_values
    print(f"{max_sequence_len = }")
    print(f"{max_sequence[0] = }")

