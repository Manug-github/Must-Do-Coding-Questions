def next_closest_time(s):
    """Program to find bext closest time with the same digits, can be repeated. 
    All Hours must be formated 00:00
    Time Complexity O(1), iterations < 24+60
    Space Complexity O(1)
    """
    hour, minute = s.split(":")
    set_digit = set([hour[0],hour[1],minute[0],minute[1]]) # Save like a Set, not neccesary max len equal 4
    minute = int(minute)+1
    add_hour = 0
    while True: # Max 60 iterations
        if minute==60:
            add_hour = 1
            minute = 0
        str_minutes = "{:02d}".format(minute)
        if str_minutes[0] in set_digit and str_minutes[1] in set_digit:
            break
        minute +=1
    hour = int(hour) + add_hour
    while True: # Max 24 iterations
        if hour==24:
            hour = 0
        str_hout = "{:02d}".format(hour)
        if str_hout[0] in set_digit and str_hout[1] in set_digit:
            break
        hour+=1
    return "{:02d}:{:02d}".format(hour,minute)
