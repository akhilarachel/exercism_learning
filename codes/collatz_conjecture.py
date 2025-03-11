def steps(number):
    iteration = 0
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    while number > 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = (number * 3) + 1
        iteration += 1

    return iteration
