import os, shutil


def insert_after(haystack, needle, new_text):
    """
    Inserts 'new_text' into 'haystack' right after 'needle' and returns the 'haystack'.
    Raises Exception if needle is not found.
    """
    i = haystack.find(needle)
    if i == -1:
        raise Exception('No substring found.')
    # start = haystack[:i+needle_length]
    # end = haystack[i+needle_length:]
    return haystack[:i+len(needle)] + new_text + haystack[i+len(needle):]


def search_files(file_extension):
    """
    Function to search files based on a given file extension in the current directory.
    Returns the names of all the files with that extension if any.
    """

    for root, dirs, files in os.walk('./.'):

        for file in files:
            extension = os.path.splitext(file)[1]
            # to get only the extension without the dot:
            # extension = os.path.splitext(file)[1][1:]

            if extension == f".{file_extension}":
                print(file)


def equality(*args):
    """
    Reads unknown number of parameters. Returns True if they have the same value or False otherwise.
    """
    for item in args[1:]:
        if args[0] != item:
            return False
    return True


def all_unique_characters3(string):
    string = ''.join(sorted(string))
    for i, char in enumerate(string[:-1]):
        if char == string[i + 1]:
            return False
    return True


def create_sorted_directory(from_folder):
    """
    Function that groups all the files, which have the same extension.
    Works only if the folder exists in the current directory otherwise raise a FileNotFoundError.
    """
    if not os.path.exists(from_folder):
        raise FileNotFoundError
    for root, dirs, files in os.walk(from_folder):
        for file in files:
            extension = os.path.splitext(file)[1][1:]
            path = f"Sorted_Directory/{extension}s"
            if not os.path.exists(path):
                os.makedirs(path)
            shutil.copy(from_folder + f'/{file}', path + f'/{file}')
            # open(path2+f'/{file}', 'a').close()   creates empty files


if __name__ == '__main__':
    # Testing
    print(insert_after("Hello World", "lo", " beautiful"))  # prints 'Hello beautiful World'
    search_files('py')
    print(equality(0, False, bool([]), not True))
    print(all_unique_characters3('How are you?'))
    create_sorted_directory(from_folder='./')
