def _map(x, min_input, max_input, min_output, max_output):
    """
    Map value between range
    """
    return ((32767 - x) - min_input) * (max_output - min_output) / (max_input - min_input) + min_output


def discrete_soil_reading(raw_analog):
    """
    Convert RAW Analog to discrete (low, normal, high) for soil moist level
    :param raw_analog: 0-32767
    :return: String moist level
    """
    status = None

    percentage = _map(raw_analog, 0, 32767, 0, 100)

    # range of soil moist level, based on percentage
    if 25 < percentage <= 100:
        status = "High"
    elif 15 <= percentage <= 25:
        status = "Normal"
    elif 0 < percentage < 15:
        status = "Low"

    return status