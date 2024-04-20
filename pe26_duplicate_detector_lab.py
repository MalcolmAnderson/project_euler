def find_repeating_portion(num_str):

    # Function to check if the potential sequence repeats throughout
    def is_valid_repeating_sequence(seq, remaining_part):
        seq_length = len(seq)
        position = 0
        end_minus_one = len(remaining_part) - 1
        while position < end_minus_one:
            for i in range(seq_length):
                comp_seq = seq[i]
                comp_rem = remaining_part[position]
                if comp_seq != comp_rem:
                    return False
                position += 1
        return True

    # Split the string into integer and fractional parts
    integer_part, fractional_part = num_str.split(".")

    len_of_fractional_part = len(fractional_part)
    for tortoise in range(len_of_fractional_part):
        for len_of_chunk in range(1, len_of_fractional_part):
            hare = tortoise
            end_current = len_of_fractional_part - len_of_chunk
            while hare < end_current:
                chunk_current = fractional_part[hare : hare + len_of_chunk]
                chunk_next = fractional_part[hare + len_of_chunk : hare + len_of_chunk * 2]
                if chunk_current == chunk_next:
                    # Potential repeating sequence found
                    remaining_part = fractional_part[hare + len_of_chunk :]
                    if is_valid_repeating_sequence(chunk_current, remaining_part):
                        # Check if the potential sequence repeats throughout
                        return chunk_current
                    else:
                        hare += 1
                else:
                    hare += 1

    return "No repeating portion"


# seq = "33"
# remaining_part = "3348963"
# print(is_valid_repeating_sequence(seq, remaining_part))

# seq = "6"
# remaining_part = "66667"
# print(is_valid_repeating_sequence(seq, remaining_part))

# Given values
lead = "0.12333348963"
repeat = "1271891287"
long_repeat = repeat * 4
test_val = lead + long_repeat

# Find the repeating portion
repeating_portion = find_repeating_portion(test_val)
print("Repeating portion:", repeating_portion)
