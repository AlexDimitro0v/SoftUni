import shutil, os
# https://knowledge.safe.com/questions/22864/startup-python-script-how-can-i-create-an-empty-fi.html
# https://thispointer.com/python-how-to-copy-files-from-one-location-to-another-using-shutil-copy/
# https://automatetheboringstuff.com/chapter9/
# https://stackoverflow.com/questions/123198/how-do-i-copy-a-file-in-python


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
            path = f"output/{extension}s"
            if not os.path.exists(path):
                os.makedirs(path)
            shutil.copy(from_folder + f'/{file}', path + f'/{file}')
            # https://www.geeksforgeeks.org/python-shutil-copyfile-method/   copyfile
            # https://www.geeksforgeeks.org/python-shutil-copy-method/       copy
            # open(path2+f'/{file}', 'a').close()   creates empty files


if __name__ == '__main__':
    create_sorted_directory(from_folder='input')
