import os


def get_folder_size(folder):
    """Function to get the size of a folder in a current directory."""
    total_size = 0
    for root, dirs, files in os.walk(f'./{folder}'):
        for file in files:
            total_size += os.stat(file).st_size
    return total_size / 1024 / 1024


def solve():
    root, dirs, files = next(os.walk('./TestFolder'))

    sizes = [os.stat(file).st_size for file in files]
    total_size = sum(sizes)

    total_size_mb = total_size / 1024 / 1024

    open('Output.txt', 'w').write(str(total_size_mb))


if __name__ == '__main__':
    open('output.txt', 'w').write(str(get_folder_size('TestFolder')))
