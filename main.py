vowels = ["A", "E", "I", "O", "U"]


def count_substring(string, sub_string):
    result = sum(1 for i in range(len(string))
                 if string.startswith(sub_string, i))
    return result


def char_is_vowel(c):
    for i in vowels:
        if c == i:
            return True
    return False


def substring_should_start_with_vowels(str):
    kevin_substring_list = []
    for i in range(len(str)):
        if char_is_vowel(str[i]):
            kevin_substring_list = generate_all_substring_start_with_char(i, str, kevin_substring_list)
    return kevin_substring_list


def kevin_substrings(str):
    list_substring = substring_should_start_with_vowels(str)
    return list_substring


def char_is_consonant(c):
    return not char_is_vowel(c)


def substring_should_start_with_consonants(str):
    stuart_substring_list = []
    for i in range(len(str)):
        if char_is_consonant(str[i]):
            stuart_substring_list = generate_all_substring_start_with_char(i, str, stuart_substring_list)
    return stuart_substring_list


def generate_all_substring_start_with_char(i, str, substring_list):
    substring = ""
    for j in range(i, len(str)):
        substring += str[j]
        substring_list.append(substring)
    return substring_list


def stuart_substrings(str):
    list_substring = substring_should_start_with_consonants(str)
    return list_substring


def calculate_score(str, substring_list):
    score = 0
    for i in substring_list:
        score += count_substring(str, i)
    return score


def minion_game(str):
    kevin_substring_list = list(set(kevin_substrings(str)))
    stuart_substring_list = list(set(stuart_substrings(str)))
    kevin_score = calculate_score(str, kevin_substring_list)
    stuart_score = calculate_score(str, stuart_substring_list)
    if kevin_score > stuart_score:
        print("Kevin {}".format(kevin_score))
    elif stuart_score > kevin_score:
        print("Stuart {}".format(stuart_score))
    else:
        print("Draw")
    pass


if __name__ == "__main__":
    str = input()
    minion_game(str)
