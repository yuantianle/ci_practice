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
        if num_str[i] in '~`!@#$%^&*()_+-=' or string.ascii_lowercase + string.ascii_uppercase:
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
