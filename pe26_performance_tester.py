import time


def manual_division_1(num, dom, places):
    output = "."
    dividend = num
    divisor = dom
    for i in range(places):
        if dividend == 0:
            break
        while divisor > dividend:
            dividend *= 10
        current = 0
        while divisor <= dividend:
            current += 1
            dividend -= divisor
        output += str(current)
    return output


def man_div_get_next_dividend(dividend, divisor):
    while divisor > dividend:
        dividend *= 10
    return dividend


def manual_division_2(num, dom, places):
    output = "0."
    dividend = num
    divisor = dom
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
    return output


def display_rc(denom):
    fraction = f"1/{denom}"
    # decimal = 1 / denom
    PLACES = 50
    decimal = manual_division(1, denom, PLACES)
    if len(decimal) < PLACES + 1:
        display = decimal
    else:
        display = decimal
        # display = get_repeating(decimal)
        # interum = decimal[: decimal.index(display[0])]
        # decimal = f"{interum}({display})"
    return f"{fraction} = {decimal}"


def validate_functionality():
    PLACES = 500
    for i in range(2, 10000):
        man_1 = manual_division_1(1, i, PLACES)
        man_2 = manual_division_2(1, i, PLACES)
        if man_1 != man_2:
            print(f"{i = }")
            print(f"{man_1 = }")
            print(f"{man_2 = }")
        if i % 100 == 0:
            print(i)


def validate_functionality_2():
    PLACES = 16
    for i in range(2, 20):
        man_1 = "{:.16f}".format(1 / i)
        man_2 = manual_division_2(1, i, PLACES)
        if man_1[:15] != man_2[:15]:
            print(f"{man_1 = } {man_2 = }")
            print(f"{len(man_1) = } {len(man_2) = }")
            print(f"{i = } ERROR DETECTED ........")
            print(f"{man_1 = }")
            print(f"{man_2 = }")
        if i % 100 == 0:
            print(i)
    print("end of run")


def test_performance():
    print(__file__)
    for function in manual_division_1, manual_division_2:
        t1 = time.perf_counter(), time.process_time()
        print(f"{t1 = }")

        # main body BEGIN
        LIMIT = 200000
        f_PRINT = False
        for denom in range(2, LIMIT):
            fraction = f"1/{denom}"
            # decimal = 1 / denom
            PLACES = 500
            decimal = function(1, denom, PLACES)
            if f_PRINT:
                if len(decimal) < PLACES + 1:
                    display = decimal
                else:
                    display = decimal
                    # display = get_repeating(decimal)
                    # interum = decimal[: decimal.index(display[0])]
                    # decimal = f"{interum}({display})"
                print(f"{fraction} = {decimal}")

        # main body END

        t2 = time.perf_counter(), time.process_time()
        print(f"{t2 = }")
        print(f"{function.__name__}()")
        print(f" Real time: {t2[0] - t1[0]:.2f} seconds")
        print(f" CPU time: {t2[1] - t1[1]:.2f} seconds")
        print()


if __name__ == "__main__":
    # print(validate_functionality())
    print(validate_functionality_2())
    # test_performance()
