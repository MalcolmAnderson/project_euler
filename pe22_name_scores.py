# import pandas as pd
import csv


def hello():
    pass


if __name__ == "__main__":
    with open("pe22_names.txt") as n:
        reader = csv.reader(n, delimiter=",", quotechar='"')
        data_read = [row for row in reader]
    names = data_read[0]
    # print(names)
    names.sort()
    grand_total = 0
    index = 0
    for name in names:
        index += 1
        print(name)
        total = 0
        for letter in name:
            ord_val = ord(letter)-ord('A')+1
            total += ord_val
        total *= index
        grand_total += total
    print(grand_total)
        
    #print(names)
    
    # my_string = "a"
    # print(ord(my_string[0])-ord('a')+1)
    