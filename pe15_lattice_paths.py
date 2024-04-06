def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)


if __name__ == "__main__":

    # 2 by 2 = 6
    width = 20
    length = 20
    # r r d d
    # r d r d
    # r d d r
    # d r r d
    # d r d r
    # d d r r

    turns = width + length

    print(factorial(turns) // factorial(width) ** 2)

    # for i in range(2):
    #     for j in range(2):
    #         print(f"{i = } {j = }")
