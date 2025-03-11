def square(number):
    grains_per_square = 1
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    if number == 1:
        return 1
    if number == 2:
        return 2
    for index in range(1, number):
        grains_per_square *= 2
    return grains_per_square


def total():
    total_grains = 0
    for index in range(1, 65):
        total_grains += square(index)
    return total_grains