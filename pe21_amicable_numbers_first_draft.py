target = 220
target_factors = [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]

def get_amicables(number):
    ret_val = [1]
    for i in range(2, number//2):
        if number % i == 0 and i**2 != number:
            ret_val.append(i)
    return ret_val

print(target_factors)
actual_factors = get_amicables(220)
print(actual_factors)
print(sum(actual_factors))

def add_factors(main, new):
    for i in new:
        if i not in main:
            main.append(i)
    return main

if __name__ == "__main__":
    number_to_be_under = 10000
    total = 0
    all_factors = []
    for i in range (number_to_be_under):
        if i % 1000 == 0:
            print(i)
        all_factors = add_factors(all_factors, get_amicables(i))
    total += sum(all_factors)
    print(total)

