# Enumerate allows us to loop over a list and retrieve both the index and the value of each item in the list
# https://stackoverflow.com/questions/2081836/reading-specific-lines-only-python


def take_odd_lines(file):
    with open(file, 'r') as r_file:
        with open('output4.txt', 'w') as w_file:
            lines = r_file.readlines()  # returns a list along with the newlines at the end
            odd_lines = [line for index, line in enumerate(lines) if index % 2 == 1]
            w_file.writelines(odd_lines)

    # open('output4.txt', 'w').write(''.join(odd_lines))  one-liner alternative


if __name__ == '__main__':
    take_odd_lines("input.txt")
