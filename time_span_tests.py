from time_span import TimeSpan

def test_make_time_span():
    manual_span_1 = TimeSpan(0, 0, 0, 0)
    manual_span_2 = TimeSpan(6, 30, 8, 0) 
    print("span_1: ", end='')
    manual_span_1.print_raw()

    print("span_2: ", end='')
    manual_span_2.print_raw()

    manual_span_2.to_military()
    print("span_2 to military: ", end='')
    manual_span_2.print_raw()

def invalid_time_span():
    try:
        bad_time = TimeSpan(10, 0, 1, 15) # 
    except:
        print('validation error caught')
        bad_time = TimeSpan(10, 0, 13, 15)
    bad_time.print_raw()
    bad_time.to_military()
    bad_time.print_raw()

def parsing_test():
    timestr = "9:30-11"
    time = TimeSpan()
    time.parse_time(timestr)
    time.print_raw()

    timestr = "7:00-123"
    time = TimeSpan()
    try:
        time.parse_time(timestr)
    except:
        print('validation error caught, 123 > 23')
    time.print_raw()

    
if __name__ == "__main__":
    test_make_time_span()
    invalid_time_span()
    parsing_test()
