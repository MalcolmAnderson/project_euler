import time


def display_timing(t1, t2):
    print("...")
    print(f" Real time: {t2[0] - t1[0]:.6f} seconds")
    print(f"  CPU time: {t2[1] - t1[1]:.6f} seconds")
    print("...")


def place_holder_for_real_code():
    pass


if __name__ == "__main__":
    t1 = time.perf_counter(), time.process_time()

    place_holder_for_real_code()

    t2 = time.perf_counter(), time.process_time()
    display_timing(t1, t2)
