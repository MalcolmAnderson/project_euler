def get_number_name(number):
    ones = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}

    tens = {
        1: "ten",
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety",
    }

    teens = {
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
    }

    str_num = str(number)
    # if len(str_num) >= 2:
    #     print(str_num[-2])
    ones_col = tens_col = hundreds_col = thousands_col = 0
    if len(str_num) > 0:
        ones_col = int(str_num[-1])
    if len(str_num) > 1:
        tens_col = int(str_num[-2])
    if len(str_num) > 2:
        hundreds_col = int(str_num[-3])
    if len(str_num) > 3:
        thousands_col = int(str_num[-4])

    ret_val = str(number) + "   ************************"
    ret_val = ""

    if number > 999:
        # ret_val += ones[thousands_col] + " thousand "
        ret_val += ones[thousands_col] + "thousand"
        number = number - number // 1000 * 1000

    if number > 99:
        # ret_val += ones[hundreds_col] + " hundred"
        ret_val += ones[hundreds_col] + "hundred"
        if number % 100 != 0:
            # ret_val += " and "
            ret_val += "and"
            number = number - (number // 100 * 100)

    if number > 0 and number < 10:
        ret_val += ones[number]
    if number < 100 and number > 9:
        if number % 10 == 0:
            ret_val += tens[tens_col]
        elif number < 20:
            ret_val += teens[number]
        else:
            # ret_val += tens[tens_col] + "-" + ones[ones_col]
            ret_val += tens[tens_col] + "" + ones[ones_col]

    return ret_val


if __name__ == "__main__":
    # long_string = get_number_name(342)

    long_string = ""
    for i in range(1, 1001):
        long_string += get_number_name(i)

    # print(long_string)
    print(len(long_string))
