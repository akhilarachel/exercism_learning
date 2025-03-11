def find_anagrams(word, candidates):
    anagram_list = []
    sorted_word = sorted(word.lower())
    for candidate in candidates:
        if sorted_word == sorted(candidate.lower()) and word.lower() != candidate.lower():
            anagram_list.append(candidate)
    return anagram_list
    pass
