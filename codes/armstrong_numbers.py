def is_armstrong_number(number):
    # digit = 0
    # number_digit = number
    number_compare = number
    total_of_digits = 0
    # while number_digit > 0:
    #     number_digit //= 10
    #     digit += 1
    # print(digit)
    # while number > 0:
    #     reminder = number % 10
    #     number //= 10
    #     total_of_digits += pow(reminder, digit)
    digit = len(str(number))
    number_string = str(number)
    for number in number_string:
        total_of_digits += pow(int(number), digit)

    return number_compare == total_of_digits
