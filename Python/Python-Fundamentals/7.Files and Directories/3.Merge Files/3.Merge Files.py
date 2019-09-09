from itertools import zip_longest


def merge_2_files(file1, file2):
    with open(file1, 'r') as r_file1:
        with open(file2, 'r') as r_file2:
            with open('write_file.txt', 'w') as w_file:
                merge = zip_longest(r_file1, r_file2)       # (1, 2) (3, 4) (5, 6) ...etc
                for pair in merge:
                    if pair[0] is not None:
                        w_file.write(pair[0])
                    if pair[1] is not None:
                        w_file.write(pair[1])


if __name__ == '__main__':
    merge_2_files('FileOne.txt', 'FileTwo.txt')
