max = 1000
for a in range(3, max - 3):
    for b in range(a + 1, max - 3):
        c = 1000 - (a + b)
        if c < b:
            break
        if a**2 + b**2 == c**2:
            print(f"{a = } {b = } {c = }")
            print(a*b*c)
