resistor_color = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
                  "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}


def label(colors):
    trio_value = ((resistor_color[colors[0]] * 10) + resistor_color[colors[1]]) * (10 ** resistor_color[colors[2]])
    # print(trio_value / 1000)
    if trio_value >= 1_000_000_000:
        return f"{int(trio_value / 1_000_000_000)} gigaohms"
    elif trio_value >= 1_000_000:
        return f"{int(trio_value / 1_000_000)} megaohms"
    elif trio_value >= 1_000:
        return f"{int(trio_value / 1_000)} kiloohms"
    return f"{trio_value} ohms"
