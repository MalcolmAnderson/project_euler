def is_number_a_palindrome(number):
    num_as_string = str(number)
    len_of_string = len(num_as_string)
    if len_of_string % 2 != 0:
        return False
    for i in range(len_of_string // 2):
        match_1 = num_as_string[i]
        match_2 = num_as_string[-(i+1)]
        if(match_1 != match_2):
            return False
    return True



def get_largest_palindrome(number):
    palindromes = []
    highest_number = 10**(number) - 1
    first_number = second_number = highest_number
    candidate_palendrome = -1
    count = 0
    highest_i = -1
    highest_j = -1
    keep_going = True
    for i in reversed(range(highest_number+1)):
        if i <= highest_j:
            break
        for j in reversed(range(highest_number+1)):
            count += 1
            candidate = i * j
            if is_number_a_palindrome(candidate):
                palindromes.append([candidate, i, j])
                if candidate_palendrome == -1:
                    candidate_palendrome = candidate
                    # highest_i = i
                    highest_j = j
                elif candidate > candidate_palendrome:
                    candidate_palendrome = candidate
                    # if highest_i < i:
                    #     highest_i = i
                    if highest_j < j:
                        highest_j = j
                break
            print(f"{i = }, {j = }, {candidate = }")
    print(palindromes)
    print(f"{count = }")
    return candidate_palendrome
                      


    return ret_val

if __name__ == "__main__":
    number_of_digits = 3
    print(f"{number_of_digits = }")
    largest_palindrome = get_largest_palindrome(number_of_digits)
    print (f"{largest_palindrome = }")
    
    # print(f"{is_number_a_palindrome(123321) = }")

