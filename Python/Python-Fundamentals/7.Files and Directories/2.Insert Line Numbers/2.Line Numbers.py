# https://stackoverflow.com/questions/8901415/readlines-not-reading-the-last-line-of-the-file-in-python


def insert_line_numbers(file):
    with open(file, 'r') as read_file:
        with open('output.txt', 'w') as write_file:
            # lines = list(read_file)        # readlines would be a less-efficient alternative
            lines = list(map(lambda line: line, read_file))
            lines_with_nums = [f"{index+1}. {line}" for index, line in enumerate(lines)]
            write_file.writelines(lines_with_nums)


# _________________________________________________________________________________________________________________________
# Reading all the lines and adding numbers to them:
def solve():
    lines = open('input.txt').read().split('\n')              # cuts the new line and store every element

    lines_with_nums = list(f'{index+1}. {line}' for index, line in enumerate(lines))

    open('output2.txt', 'w').write('\n'.join(lines_with_nums))


if __name__ == '__main__':
    insert_line_numbers('input.txt')
