def round_ans(val):
    """
    Rounds temperatures to nearest integer
    """
    var_rounded = (val * 2 + 1) // 2
    return "{:.0f}".format(var_rounded)


def to_kilometers(to_convert):
    """
    Converts from Miles to Kilometers
    """
    answer = (to_convert * 1.609344)
    return round_ans(answer)


def to_miles(to_convert):
    """
    Converts from Kilometers to Miles
    """
    answer = to_convert * 0.621371
    return round_ans(answer)


