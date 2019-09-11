# Creating private functions to check if word is upper_case or lower_case,
# because special characters are not caught by the built-in functions.


# ______________________
def is_upper(word):
    """
    Return True if the string is an uppercase string, False otherwise.
    A string is uppercase if all cased characters in the string are uppercase and there is at least one
    cased character in the string.

    :param word: iterable string
    :return: bool
    """
    if not word:
        return False
    for letter in word:
        if not ord("A") <= ord(letter) <= ord("Z"):
            return False
    return True


def is_lower(word):
    """
    Return True if the string is a lowercase string, False otherwise.
    A string is lowercase if all cased characters in the string are lowercase and there is at least one
    cased character in the string.

    :param word: iterable string
    :return: bool
    """
    if not word:
        return False
    for letter in word:
        if not ord("a") <= ord(letter) <= ord("z"):
            return False
    return True
# __________________________


def solve1(data):
    upper_case = []
    lower_case = []
    mixed_case = []
    for item in data.split():
        if is_lower(item):
            lower_case += [item]
        elif is_upper(item):
            upper_case += [item]
        else:  # mixed_case
            mixed_case += [item]

    print(f"Lower-case: {', '.join(lower_case)}")
    print(f"Mixed-case: {', '.join(mixed_case)}")
    print(f"Upper-case: {', '.join(upper_case)}")


# another way
# ======================================================================================================================
def solve2(data):
    word_list = data.split()
    case_list = [['Lower-case:'], ['Mixed-case:'], ['Upper-case:']]
    for word in word_list:
        have_mixed_char = False  		# create a flag for the special symbols
        if not str(word).isalpha():		# if does not contain only letters
            have_mixed_char = True
        if word.islower() and not have_mixed_char:
            case_list[0].append(word)
        elif word.isupper() and not have_mixed_char:
            case_list[2].append(word)
        else:
            case_list[1].append(word)

    for i in range(len(case_list)):
        print(print_result(case_list[i]))


def print_result(case_words):
    case_string = ', '.join(case_words[1:])
    result = case_words[0] + ' ' + case_string
    return result
# ======================================================================================================================


def main():
    data = input()
    list_separators = [",", ";", ":", ".", "!", "(", ")", "\"", "\'", "\\", "/", "[", "]", " "]
    for separator in list_separators:
        data = data.replace(separator, ' ')
    solve1(data)


if __name__ == '__main__':
    main()
