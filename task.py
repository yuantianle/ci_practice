def my_datetime(num_sec):
    year_cnt = 1970
    date_cnt = 1
    month_cnt = 1
    sec_copy = num_sec
    
    leap_y_flag = 3
    days_flag = 365
    while sec_copy % days_flag != 0:
        sec_copy = sec_copy % days_flag
        year_cnt += 1
        leap_y_flag += 1
        if leap_y_flag % 4 == 0:
            days_flag = 366
        else:
            days_flag = 365
    print("Years", year_cnt)
    print("Remaining months", sec_copy)
    return date_time_str
