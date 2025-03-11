def resistor_label(colors):
    resistor_color = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
                      "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}
    tolerance = {"grey": "±0.05%", "violet": "±0.1%", "blue": "±0.25%", "green": "±0.5%",
                 "brown": "±1%", "red": "±2%", "gold": "±5%", "silver": "±10%"}

    if len(colors) == 1:
        return f"{resistor_color[colors[0]]} ohms"

    if len(colors) > 4:
        color_value = (resistor_color[colors[0]] * 100) + (resistor_color[colors[1]] * 10) + resistor_color[colors[2]]
        multiplier = 10 ** resistor_color[colors[3]]
    else:
        color_value = (resistor_color[colors[0]] * 10) + resistor_color[colors[1]]
        multiplier = 10 ** resistor_color[colors[2]]

    resistance = color_value * multiplier

    if resistance >= 1_000_000_000:
        resistance_str = f"{resistance / 1_000_000_000}"
        unit = "gigaohms"
    elif resistance >= 1_000_000:
        resistance_str = f"{resistance / 1_000_000}"
        unit = "megaohms"
    elif resistance >= 1_000:
        resistance_str = f"{resistance / 1_000}"
        unit = "kiloohms"
    else:
        resistance_str = f"{resistance}"
        unit = "ohms"

    if ".0" in resistance_str:
        resistance_str = resistance_str.rstrip(".0")
    tol = tolerance.get(colors[-1], "")
    return f"{resistance_str} {unit} {tol}".strip()
