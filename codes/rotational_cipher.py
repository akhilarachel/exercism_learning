import string


def rotate(text, key):
    if not text:
        return None
    if key % 26 == 0:  # Handles key = 0 and key = 26 cases
        return text

    lower_char = string.ascii_lowercase
    upper_char = string.ascii_uppercase
    new_word = []

    for letter in text:
        if letter.islower():
            new_word.append(lower_char[(lower_char.index(letter) + key) % 26])
        elif letter.isupper():
            new_word.append(upper_char[(upper_char.index(letter) + key) % 26])
        else:
            new_word.append(letter)

    return "".join(new_word)
