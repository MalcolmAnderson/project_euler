import time as t

# fmt: off
# fmt: on


def main():
    pass


def print_time(seconds):
    hour_seconds = 60 * 60
    days_seconds = 24 * hour_seconds
    ret_val = ""
    hours_lead_zero = False
    minutes_lead_zero = False
    seconds_lead_zero = False
    if seconds < 2:
        # str_sec = str(seconds)
        # no_space_str_sec = str_sec[1:]
        ret_val = f"{seconds:0.6f} seconds"
    else:
        if seconds >= days_seconds:
            hours_lead_zero = True
            days = int(seconds // days_seconds)
            seconds -= days * days_seconds
            ret_val += str(days) + "d-"
        if seconds >= hour_seconds:
            minutes_lead_zero
            hours = int(seconds // hour_seconds)
            seconds -= hours * hour_seconds
            if hours < 10 and hours_lead_zero:
                ret_val += "0" + str(hours)
            else:
                ret_val += str(hours)
            ret_val += ":"
        if seconds > 60:  # minutes
            minutes = int(seconds // 60)
            seconds -= minutes * 60
            if minutes_lead_zero:
                ret_val += f"{minutes:02}:"
            else:
                ret_val += f"{minutes}:"
            seconds_lead_zero = True
        if seconds > 1:
            frac_seconds = str(seconds % 1)
            frac_second = frac_seconds[2:]
            seconds = int(seconds // 1)
            if seconds_lead_zero:
                disp_seconds = f"{seconds:02}"
            else:
                disp_seconds = f"{seconds}"
            ret_val += f"{disp_seconds}.{frac_second[:2]}"

    return ret_val


if __name__ == "__main__":
    # start_time = t.time()  # get start time
    # main()
    # end_time = t.time()  # get end time

    # total_time = end_time - start_time
    # print(total_time)

    test = ".789379857"
    print(test[1:])

    print("******")
    print(f'test1 - "{print_time(0.21398759)}"')
    print(f'test2 - "{print_time(1.21398759)}"')

    print(f"test3 - {print_time(2.21398759)} seconds")

    print(f"test4 1:12.21 - {print_time(72.21398759)}")

    print(f"test5 1d-03:09:02.21 - {print_time(97742.21398759)}")

    seconds = 372.03892
    converted = t.strftime("%H:%M:%S.%f", t.gmtime(seconds))
    print(converted)
