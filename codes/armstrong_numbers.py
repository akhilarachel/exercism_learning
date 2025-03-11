def is_armstrong_number(number):
    digit = 0
    number_compare = number
    number_digit = number
    total_of_digits = 0
    while number_digit > 0:
        number_digit //= 10
        digit += 1
    print(digit)
    while number > 0:
        reminder = number % 10
        number //= 10
        total_of_digits += pow(reminder, digit)

    return number_compare == total_of_digits
