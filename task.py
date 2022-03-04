import string


def f1_transfer_digit(num_str, minus_flag):
    llen = len(num_str)
    sum = 0
    for i in range(llen):
        sum += int(num_str[i]) * pow(10, (llen - i - 1))
    if minus_flag:
        return -sum
    else:
        return sum


def f1_transfer_float(num_str, minus_flag):
    float_flag = 0
    point_index = -1
    for i in range(len(num_str)):
        if num_str[i] in ('~`!@#$%^&*()_+-=' + string.ascii_lowercase + string.ascii_uppercase):
            return None
        elif num_str[i] == ".":
            if float_flag < 1:
                float_flag += 1
                point_index = i
            else:
                return None
    sum = 0.0
    Positionflag = 0
    for i in range(point_index - 1, -1, -1):
        sum += (int(num_str[i])) * pow(10, Positionflag)
        Positionflag += 1
    Positionflag = 1
    for i in range(point_index + 1, len(num_str)):
        sum += (int(num_str[i])) * pow(10, -Positionflag)
        Positionflag += 1
    if minus_flag:
        return -sum
    else:
        return sum


def f1_transfer_hex(num_str, minus_flag):
    hexset = dict({'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                   '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
                   'D': 13, 'E': 14, 'F': 15, 'a': 10, 'b': 11, 'c': 12, 'd': 13,
                   'e': 14, 'f': 15})

    ssum = 0
    for i in range(2, len(num_str)):
        if num_str[i] not in hexset:
            return None
        else:
            hex = hexset[num_str[i]]
            digit = pow(16, len(num_str) - 2 - (i - 2) - 1)
            ssum += hex * digit
    if minus_flag:
        return -ssum
    else:
        return ssum


def conv_num(num_str):
    minus_flag = False
    if num_str[0] == '-':
        num_str = num_str[1:]
        minus_flag = True

    if num_str.isdigit():
        return f1_transfer_digit(num_str, minus_flag)

    if (num_str[0] == '0') and (num_str[1] == 'x' or 'X'):
        return f1_transfer_hex(num_str, minus_flag)
    else:
        return f1_transfer_float(num_str, minus_flag)


def days_in_month(month, leap_yr=False):
    # Function to return number of days in a month based on leap year
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    if month == 2:
        if leap_yr:
            return 29
        return 28
    return 30


def date_yrs_days(num_sec):
    # Function to covert seconds to nearest number of years
    days = num_sec / (60 * 60 * 24)
    yrs = days / 365.24
    return yrs


def check_if_lp(yr):
    # Function to check if a given year is a leap year or not
    if (
        ((yr % 400 == 0) and (yr % 100 == 0)) or
        ((yr % 4 == 0) and (yr % 100 != 0))
       ):
        return True
    return False


def app_zero(num):
    # Function to append a zero to date if single digit
    str_num = str(num)
    if len(str_num) < 2:
        return '0'+str_num
    return str_num


def get_days(num_sec, years):
    # Given seconds and latest year, compute days and month
    num_days_till_year = 0
    for yr in range(1970, years):
        if check_if_lp(yr):
            num_days_till_year += 366
        else:
            num_days_till_year += 365
    num_days_till_year -= 1
    num_sec -= (num_days_till_year*86400)
    num_days_till_months = 0
    flag = -1
    mn_flow = 0
    while flag < 0:
        if (num_sec - days_in_month(mn_flow+1, check_if_lp(years))*86400) > 0:
            mn_flow += 1
            num_sec -= days_in_month(mn_flow, check_if_lp(years))*86400
        else:
            mn_flow += 1
            flag = 1
    total_days = num_sec / 86400
    return total_days, mn_flow


def date_time(num_sec):
    # Driver function for converting seconds to date from epoch
    final_yrs = date_yrs_days(num_sec)
    rn_yrs = divmod(final_yrs, 1)[0]
    yrs_current = int(1970 + rn_yrs)

    dy, month = get_days(num_sec, yrs_current)
    if month < 1:
        month = 1
    if dy == 0:
        dy = 1
    return "{}-{}-{}".format(app_zero(month), app_zero(int(dy)), yrs_current)


def reverse_bytes(reminder_list, even_len=True):
    '''Function to reverse reminder list for every two characters'''
    last_ind = 0
    final_bytes = []
    final_str = ''
    if even_len:
        list_len = len(reminder_list)+1
    else:
        list_len = len(reminder_list)
    for i in range(2, list_len, 2):
        tmp_list = list(reminder_list[last_ind: i])
        tmp_list.reverse()
        string_tmp = [str(ch) for ch in tmp_list]
        final_str = final_str.join(string_tmp)
        final_bytes.append("".join(string_tmp))
        last_ind = i
    return final_bytes, last_ind


def decide_pos_neg(num, final_bytes):
    '''Function to decide if a given number is pos or negative'''
    if num < 0:
        return "-" + " ".join(final_bytes)
    else:
        return " ".join(final_bytes)


def conv_endian(num, endian='big'):
    '''Main function for converting decimal to hexadecimal'''
    # Conversion dictionary for numbers larger than 9
    conv_dict = {10: 'A', 11: 'B',  12: 'C',  13: 'D',
                 14: 'E', 15: 'F', 16: 'G'}
    if endian not in ['big', 'little']:
        # Return None if endian type is invalid
        return None
    # Removing sign of number and deal with it later
    copy_num = abs(num)
    # Using reminder method to aggregate reminders
    q = copy_num
    rem_list = []
    while q != 0:
        q, rem = divmod(q, 16)
        if rem > 9:
            # Only convert to Hex values when above 9
            rem = conv_dict[rem]
        rem_list.append(rem)
    # For odd length reminders we need to append a zero
    if len(rem_list) % 2 != 0:
        final_bytes, last_ind = reverse_bytes(rem_list, False)
        if (len(rem_list) - last_ind) > 0:
            tmpb = "0" + str(rem_list[-1])
            final_bytes.append(tmpb)
    # For even length reminders we can use it directly
    else:
        final_bytes, last_ind = reverse_bytes(rem_list, True)

    # Reverse for big endian and append sign to the start if negative
    if endian == 'big':
        final_bytes.reverse()
        return decide_pos_neg(num, final_bytes)

    if endian == 'little':
        return decide_pos_neg(num, final_bytes)
