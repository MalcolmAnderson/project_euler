def fact(num):
    total = 1
    for i in range(1, num + 1):
        total *= i
    return total


if __name__ == "__main__":
    # print(fact(2))
    inputs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 1000000
    num_before = 0
    output = []
    len_inputs = len(inputs)
    for i in range(9, 0, -1):  # 9 -> 0
        i_fact = fact(i)
        count = 0
        while num_before + i_fact < target:
            count += 1
            num_before += i_fact
        if num_before + i_fact >= target:
            output.append(inputs[count])
            del inputs[count]
    output.append(inputs[0])
    del inputs[0]

    print(output)
    str_list = [str(x) for x in output]
    print(str_list)
    int_list = int("".join(str_list))
    print(int_list)
