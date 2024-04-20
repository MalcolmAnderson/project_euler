arr = []

for d in range(1, 1000):
    num = 1 / d
    if len(str(num)) >= 1:
        arr.append(num)


cnt = 0

for ch in arr:
    cnt += 1
    if len(str(ch)[2:]) == 16:
        if str(ch)[2:10] == str(ch)[10:18]:
            print(f"{cnt}) {ch} --> {len(str(ch)[2:])}")
