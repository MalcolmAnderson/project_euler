def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)
    
num_factorial = factorial(100)
str_num = str(num_factorial)
total = 0
for i in str_num:
    total += int(i)
print(total)