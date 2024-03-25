# Python program to display the Fibonacci sequence

def recur_fibo(n):
    print(f"recur_fibo called with {n = }")
    if n <= 1:
        return n
    else:
        minus_1 = recur_fibo(n-1)
        minus_2 = recur_fibo(n-2)
        # return(recur_fibo(n-1) + recur_fibo(n-2))
        print(f"return {minus_1 + minus_2} - {minus_1 = } {minus_2 = }")
        return (minus_1 + minus_2)

nterms = 5

# check if the number of terms is valid
if nterms <= 0:
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(1, nterms):
        print(f"{recur_fibo(i) = }")




