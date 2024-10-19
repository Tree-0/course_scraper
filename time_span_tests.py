from time_span import TimeSpan

def test_make_time_span():
    manual_span_1 = TimeSpan(0, 0, 0, 0)
    manual_span_2 = TimeSpan(6, 30, 8, 0) 
    print("span_1: ", end='')
    print(manual_span_1.__str__())

    print("span_2: ", end='')
    print(manual_span_2.__str__())

    manual_span_2.to_military()
    print("span_2 to military: ", end='')
    print(manual_span_2.__str__())

def invalid_time_span():
    try:
        bad_time = TimeSpan(10, 0, 1, 15) # 
    except:
        print('validation error caught')
        bad_time = TimeSpan(10, 0, 13, 15)
    print(bad_time.__str__())
    bad_time.to_military()
    print(bad_time.__str__())

def parsing_test():
    timestr = "9:30-11"
    time = TimeSpan()
    time.parse_time(timestr)
    print(time.__str__())

    timestr = "7:00-123"
    time = TimeSpan()
    try:
        time.parse_time(timestr)
    except:
        print('validation error caught, 123 > 23')
    print(time.__str__())

    
if __name__ == "__main__":
    test_make_time_span()
    invalid_time_span()
    parsing_test()
