def test_array_add():
    a1 = [0, 9, 0]
    a2 = [0, 1, 1]
    actual = array_add(a1, a2)
    expected = [0, 0, 1]
    print(f"{expected = } {actual = }")
    assert expected == actual


def array_add(a1, a2):
    len_of_a2 = len(a2)
    ret_val = [0] * len_of_a2
    for i in range(len_of_a2 - 1, 0, -1):
        current = a1[i] + a2[i] + ret_val[i]
        if current >= 10:
            ret_val[i - 1] = 1
            current -= 10
        ret_val[i] = current
    return ret_val


def index_of_fibonacci_of_len(digits):
    first = second = [0] * digits
    first[-1] = 1
    second[-1] = 1
    count = 2
    while second[0] == 0:
        count += 1
        if count % 10 == 0:
            print(count)
        new_second = array_add(first, second)
        first = second
        second = new_second
    return count


if __name__ == "__main__":
    actual = index_of_fibonacci_of_len(1000)
    expected = 12
    print(f"{expected = } {actual = }")
