# given a time in the from #:## or ##:## in 24 hour format
def main():
    print(convert(input("What time is it?: ")))

def convert(time):
    time_list = time.split(":")
    hour = int(time_list[0])
    minute = float(int(time_list[1])/60)
    current_time = hour + minute

    if current_time <= 8.00 and current_time >= 7.00:
        return "breakfast time"
    elif current_time <= 13.00 and current_time >= 12.00:
        return "lunch time"
    elif current_time <= 19.00 and current_time >= 18.00:
        return "dinner time"
    else:
        return "not meal time yet"

if __name__ == "__main__":
    main()