def is_isogram(string):

    text = string.lower()
    for letter in text:
        if letter.isalpha():
            # print(letter)
            letter_count = text.count(letter)
            # print(letter_count)
            if letter_count > 1:
                return False
    return True


print(is_isogram("lumberjacks"))