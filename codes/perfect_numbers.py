def classify(number):
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    divisor_sum = 0
    for index in range(1, number):
        if number % index == 0:
            divisor_sum += index
    if divisor_sum == number:
        return "perfect"
    elif divisor_sum < number:
        return "deficient"
    else:
        return "abundant"
    