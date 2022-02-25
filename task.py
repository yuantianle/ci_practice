# import string

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
        if num_str[i] in '~`!@#$%^&*()_+-=':
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
    hexset = ['0', '1', '2', '3', '4', '5', '6',
              '7', '8', '9', '10', 'A', 'B', 'C',
              'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f']

    for i in range(len(num_str)):
        if i != 0 and i != 1 and num_str[i] not in hexset:
            return None
    return None


def conv_num(num_str):
    minus_flag = False
    if num_str[0] == '-':
        num_str = num_str[1:]
        minus_flag = True

    if num_str.isdigit():
        f1_transfer_digit(num_str, minus_flag)

    if (num_str[0] == '0') and (num_str[1] == 'x'):
        f1_transfer_float(num_str, minus_flag)
    else:
        f1_transfer_hex(num_str, minus_flag)
