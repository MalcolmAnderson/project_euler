def sum_of_squares(num):
    total = 0
    for i in range(1, num + 1):
        total += i**2
    return total

def square_of_sums(num):
    total = 0
    for i in range(1, num + 1):
        total += i
    return total**2

if __name__ == "__main__":
    num = 100
    sum = sum_of_squares(num)
    print(f"{   sum = }")
    square = square_of_sums(num)
    print(f"{square = }")
    print(f"difference = {square - sum}")
