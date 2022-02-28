def days_in_month(month, leap_yr=False):
    # Return number of days in month for both leap and non-leap year
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    if month == 2:
        if leap_yr:
            return 29
        return 28
    return 30

def date_yrs_days(num_sec):
    # Convert seconds into year and month
    days = num_sec / (60* 60*24)
    yrs = days/ 365.24
    months = round((yrs%1)*12)
    frac_days = ((yrs%1)*12)%1
    return yrs, months, frac_days

def get_days(num_sec, years, months):
    # Convert seconds into day
    # Issues prediciting date for anything after current date
    total_days = int(divmod((num_sec / (60* 60*24)), 1)[0]) + 1    
    for yr in range(1970, years):
        if (yr % 4 == 0 or yr % 400 == 0 or yr % 100 == 0):
            total_days = total_days - 366
        else: 
            total_days = total_days - 365
    for mn in range(1, months):
        if (years % 4 == 0 or years % 400 == 0 or yr % 100 == 0):
            days_in_m = days_in_month(mn, True)
            total_days -= days_in_m
        else:
            days_in_m = days_in_month(mn, False)
            total_days -= days_in_m 
    return total_days

def date_time(num_sec):
    final_yrs, month, f_days = date_yrs_days(num_sec)
    rnd_yrs = divmod(final_yrs, 1)[0]
    yrs_current = int(1970 + rnd_yrs)
    if month < 1:
        month = 1
    # Issues prediciting date here
    dy = get_days(num_sec, yrs_current, month)
    if dy == 0:
        dy = 1
    return "{}-{}-{}".format(month, dy, yrs_current)
print(date_time(seconds))
