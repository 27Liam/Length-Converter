def round_ans(val):
    """
    Rounds floats UP to nearest integer
    """
    var_rounded = (val * 2 + 1) // 2
    return "{:.0f}".format(var_rounded)


def to_kilometers(to_convert):
    """
    Converts from miles to kilometers
    """
    answer = (to_convert - 32) * 5 / 9
    return round_ans(answer)


def to_miles(to_convert):
    """
    Converts from kilometers to miles
    """
    answer = to_convert * 1.8 + 32
    return round_ans(answer)