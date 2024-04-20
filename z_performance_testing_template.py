import time


def sleeper():
    time.sleep(1.75)


def spinlock():
    for _ in range(100_000_000):
        pass


print(__file__)
for function in sleeper, spinlock:
    t1 = time.perf_counter(), time.process_time()
    print(f"{t1 = }")
    function()
    t2 = time.perf_counter(), time.process_time()
    print(f"{t2 = }")
    print(f"{function.__name__}()")
    print(f" Real time: {t2[0] - t1[0]:.2f} seconds")
    print(f" CPU time: {t2[1] - t1[1]:.2f} seconds")
    print()
# sleeper()
#  Real time: 1.75 seconds
#  CPU time: 0.00 seconds

# spinlock()
#  Real time: 1.77 seconds
#  CPU time: 1.77 seconds
