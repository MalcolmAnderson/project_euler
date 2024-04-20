import time

OUTPUT_START = "0."
PLACES = 10_000
LONGEST_POSSIBLE_CANDIDATE = 1000


def display_timing(t1, t2, repeating_function):
    print("...")
    print(f"{repeating_function.__name__}()")
    print(f" Real time: {t2[0] - t1[0]:.6f} seconds")
    print(f"  CPU time: {t2[1] - t1[1]:.6f} seconds")
    print("...")


# Function to check if the potential sequence repeats throughout
# Function assumes that there is no rounding on the last char
# recommend removing last char of fraction before using.
def is_valid_repeating_sequence(seq, remaining_part):
    if len(remaining_part) == 1:
        return False
    seq_length = len(seq)
    position = 0
    # end_minus_seq_length = len(remaining_part) - seq_length
    # while position < end_minus_seq_length:
    len_remaining_part = len(remaining_part)
    duplicate_count = 0
    if seq_length < 10:
        term_count = 5
    else:
        term_count = 2
    while position < len_remaining_part:
        for i in range(seq_length):
            if position >= len_remaining_part:
                break
            comp_seq = seq[i]
            comp_rem = remaining_part[position]
            if comp_seq != comp_rem:
                return False
            position += 1
        duplicate_count = +1
        if duplicate_count >= term_count:
            return True
    return True


# def find_repeating_portion_0(num_str):
#     # Split the string into integer and fractional parts
#     integer_part, fractional_part = num_str.split(".")
#     # strip off the last char to handle rounding
#     fractional_part = fractional_part[: len(fractional_part) - 1]
#     len_of_fractional_part = len(fractional_part)
#     for tortoise in range(len_of_fractional_part):
#         for len_of_chunk in range(1, len_of_fractional_part):
#             hare = tortoise
#             end_current = len_of_fractional_part - len_of_chunk
#             while hare < end_current:
#                 chunk_current = fractional_part[hare : hare + len_of_chunk]
#                 chunk_next = fractional_part[hare + len_of_chunk : hare + len_of_chunk * 2]
#                 if chunk_current == chunk_next:
#                     # Potential repeating sequence found
#                     remaining_part = fractional_part[hare + len_of_chunk :]
#                     if is_valid_repeating_sequence(chunk_current, remaining_part):
#                         # Check if the potential sequence repeats throughout
#                         return chunk_current
#                     else:
#                         hare += 1
#                 else:
#                     hare += 1

#     return num_str


def find_repeating_portion(str_of_num):
    # print("hello")
    # print(ord("."))
    # print(type(str_of_num))
    # print(str_of_num[0])
    # print(ord(str_of_num[1]))
    if "." in str_of_num:
        integer_part, fractional_part = str_of_num.split(".")
        list_of_num = list(fractional_part)
    else:
        list_of_num = list(str_of_num)
    candidate = []
    cand_rest = []
    len_of_str = len(list_of_num)
    for tortois in range(len_of_str):
        candidate = [list_of_num[tortois]]  # start run with first char of cur location
        cand_rest = list_of_num[tortois + 1 :]
        len_of_rest = len(cand_rest)
        # TODO change this for to an appropriate while loop
        for i in range(len_of_rest):
            # if candidate is too long, prevent false positive with short sequence at end of cand_rest
            if len(candidate) > LONGEST_POSSIBLE_CANDIDATE:
                break
            if is_valid_repeating_sequence(candidate, cand_rest):
                ret_val = "".join([str(x) for x in candidate])
                return ret_val
            else:
                candidate.append(cand_rest[0])
                del cand_rest[0]
    return str_of_num


def manual_division(dividend, divisor, places=PLACES, display=False):
    output = OUTPUT_START
    repeat = -1
    for i in range(places):
        if dividend == 0:
            break
        # handle leading zeros
        added_zeros = 0
        while divisor > dividend:
            added_zeros += 1
            dividend *= 10
            if added_zeros > 1:
                output += "0"
        # do division
        current = dividend // divisor
        dividend = dividend % divisor
        output += str(current)
        # TODO put hook here to check for "2 complete duplicates"
    if display:
        print(f"{dividend}/{divisor}")
        print(f"     {output = }")
        print(f"     {repeat = }")
    return output, repeat


def display_rc(denom, display=False, repeating_function=find_repeating_portion):
    fraction = f"1/{denom}"
    # decimal = 1 / denom
    decimal, repeat = manual_division(1, denom, PLACES, display)
    if len(decimal) < PLACES + len(OUTPUT_START):
        display = decimal
    else:
        display = decimal
        display = repeating_function(decimal)
        interum = decimal[: decimal.index(display)]
        decimal = f"{interum}({display})"
    return f"{fraction} = {decimal}", display


def main(low=2, high=1000, display=False, repeating_function=find_repeating_portion):
    # LIMIT = 1010
    results = []
    longest = [-1, -1, -1]  # denominator, repeating, length

    for denom in range(low, high):  # yes, this does NOT process "high"
        if denom % 10 == 0:
            print(denom)
        readable_display, repeating = display_rc(denom, display, repeating_function)
        if display:
            print(readable_display)
        if len(repeating) > longest[2] and len(repeating) > 0:
            longest = [denom, repeating, len(repeating)]
            summary = [denom, len(repeating), repeating[:20]]
            # results.append(summary)
            if display:
                print(longest[0], longest[2])
            else:
                print(longest)
    return results
    # # print(display_rc(denom))
    # print(f"{len(repeating) =} {readable_display}")


if __name__ == "__main__":
    # list_of_repeating_functions = [find_repeating_portion, find_dup_lab]
    # list_of_repeating_functions = [find_repeating_portion]
    list_of_repeating_functions = [find_repeating_portion]
    for repeating_function in list_of_repeating_functions:
        t1 = time.perf_counter(), time.process_time()

        # main(low=983, high=984, display=False, repeating_function=repeating_function)
        results = main(low=2, high=1000, display=False, repeating_function=repeating_function)
        # results exists to save results for futher analysis
        # print(results)
        # test = ".123472347234"
        # print(get_repeating(test))

        # useful test
        # test = display_rc(11)
        # print(f"expected = 0.(09),       actual = {test}")
        # test = display_rc(17)
        # print(f"expected = 0.588235294,  actual = {test}")
        # test = display_rc(19)
        # print(f"expected = 0.0526315789, actual = {test}")
        # print(test)

        # useful test
        # print(f"1/9 expected = .(52631578947368421) - actual = {find_repeating_portion("0.52631578947368421526315789473684215263157894736842")}")

        t2 = time.perf_counter(), time.process_time()
        display_timing(t1, t2, repeating_function)
