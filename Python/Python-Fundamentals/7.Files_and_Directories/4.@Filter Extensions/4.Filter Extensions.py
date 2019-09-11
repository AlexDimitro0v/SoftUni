import os


def search_files(file_extension):
    """Function to search files based on a given file extension in the current directory"""
    """
    :return the names of all the files with that extension
    """
    # debug = list(os.walk('./input'))
    # print(debug)
    for root, dirs, files in os.walk('./.'):
        # print(root)
        # print(dirs)
        # print(files)

        for file in files:
            # https://stackoverflow.com/questions/541390/extracting-extension-from-filename-in-python

            # extension = file.split(".")[-1]       alternative
            extension = os.path.splitext(file)[1]
            # to get only the extension without the dot:
            # extension = os.path.splitext(file)[1][1:]

            if extension == f".{file_extension}":
                print(file)


if __name__ == '__main__':
    data = input('Enter the file extension you are searching for: ')
    search_files(file_extension=data)
