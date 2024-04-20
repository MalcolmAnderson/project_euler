import time


def display_timing(t1, t2):
    print("...")
    print(f" Real time: {t2[0] - t1[0]:.6f} seconds")
    print(f"  CPU time: {t2[1] - t1[1]:.6f} seconds")
    print("...")


# triangle_manual = [
#     [75],
#     [95, 64],
#     [17, 47, 82],
#     [18, 35, 87, 10],
#     [20, 4, 82, 47, 65],
#     [19, 1, 23, 75, 3, 34],
#     [88, 2, 77, 73, 7, 63, 67],
#     [99, 65, 4, 28, 6, 16, 70, 92],
#     [41, 41, 26, 56, 83, 40, 80, 70, 33],
#     [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
#     [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
#     [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
#     [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
#     [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
#     [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
# ]


def main():
    triangle_raw = """
    75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
    """
    # create our rows
    tri_parsed = triangle_raw.strip().split("\n")
    # convert each row into a list of values
    for i in range(len(tri_parsed)):
        tri_parsed[i] = tri_parsed[i].strip().split(" ")
        # convert each value from string to int
        for j in range(len(tri_parsed[i])):
            tri_parsed[i][j] = int(tri_parsed[i][j])

    # start at second to last row of triangle
    current_row = len(tri_parsed) - 2

    # row loop
    for i in range(current_row, -1, -1):  # current row
        for j in range(0, i + 1):  # next row - i + 1 because "next row" has 1 more col than current row
            down_left = tri_parsed[i + 1][j]
            down_right = tri_parsed[i + 1][j + 1]
            current_number = tri_parsed[i][j]
            if down_left > down_right:
                tri_parsed[i][j] += down_left
            else:
                tri_parsed[i][j] += down_right

    for row in tri_parsed:
        print(row)
    print(tri_parsed[0][0])


if __name__ == "__main__":
    t1 = time.perf_counter(), time.process_time()

    main()

    t2 = time.perf_counter(), time.process_time()
    display_timing(t1, t2)
