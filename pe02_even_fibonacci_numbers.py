fib_nums = [1, 2]
first = 1
second = 2
while first + second <= 4000000:
    if first % 1000 == 0:
        print(first)
    new_second = first + second
    fib_nums.append(new_second)
    first = second
    second = new_second
total = 0
for i in fib_nums:
    if i % 2 == 0:
        total += i
print(total)