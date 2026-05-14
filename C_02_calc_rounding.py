def round_ans(val):
    """
    Rounds floats UP to nearest integer
    """
    var_rounded = (val * 2 + 1) // 2
    return "{:.0f}".format(var_rounded)


def to_celsius(to_convert):
    """
    Converts from degrees °F to °C
    """
    answer = (to_convert - 32) * 5 / 9
    return round_ans(answer)


def to_fahrenheit(to_convert):
    """
    Converts from °F to °C
    """
    answer = to_convert * 1.8 + 32
    return round_ans(answer)


to_c_test = [0, 100, -459]
to_f_test = [0, 100, 40, -273]

for item in to_f_test:
    print(f"{item} C is {to_fahrenheit(item)} F")

print()

for item in to_c_test:
    print(f"{item} F is {to_celsius(item)} C")
