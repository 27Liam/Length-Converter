def round_ans(val):
    """
    Rounds temperatures to nearest degree
    :param val: Number to be rounded
    :return: Number rounded to nearest degree
    """
    var_rounded = (val * 2 + 1) // 2
    return "{:.0f}".format(var_rounded)


def to_kilometers(to_convert):
    """
    Converts from Miles to Kilometers
    :param to_convert: Temperature to be converted in °F
    :return:  Converted temperature in °C
    """
    answer = (to_convert * 1.609344)
    return round_ans(answer)


def to_miles(to_convert):
    """
    Converts from Kilometers to Miles
    :param to_convert: Temperature to be converted in °C
    :return:  Converted temperature in °F
    """
    answer = to_convert * 0.621371
    return round_ans(answer)


# Main Routine / Testing starts here
# to_c_test = [0, 100, -459]
# to_f_test = [0, 100, 40, -273]
#
# for item in to_f_test:
#     ans = to_fahrenheit(item)
#     print(f"{item} C is {ans} F")
#
# print()
#
# for item in to_c_test:
#     ans = to_celsius(item)
#     print(f"{item} F is {ans} C")
