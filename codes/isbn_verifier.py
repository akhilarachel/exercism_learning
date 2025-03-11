def is_valid(isbn):
    index = 10
    total_value = 0
    new_isbn = isbn.replace('-', '')

    for letter in new_isbn:
        if (letter == 'X' or letter == 'x') and index == 1:
            letter = '10'
        if letter.isdigit():
            total_value = total_value + (int(letter) * index)
            index -= 1
        else:
            return False

    if total_value % 11 == 0 and index == 0:
        return True
    return False
