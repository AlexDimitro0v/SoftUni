def main():
    nums = list(map(int, input().split()))
    data = input()
    while data != 'END':
        command = data.split()[0]
        if command == 'multiply':
            command2 = data.split()[1]
            if command2 == 'list':
                command3 = int(data.split()[2])
                nums = nums * command3
            else:
                element = int(data.split()[1])
                command3 = int(data.split()[2])
                nums = [n*command3 if element == n else n for n in nums]                      # lst compre. solution
                # nums = list(map(lambda n: n*command3 if n == element else n, my_list))      # map solution
        elif command == 'contains':
            element = int(data.split()[1])
            if element in nums:
                print('True')
            else:
                print('False')
        elif command == 'add':
            command2 = data.split()[1]
            elements = list(map(int, command2.split(',')))
            # nums.extend(elements)
            nums += elements
        data = input()
    # print(*nums, sep=' ')
    print(' '.join(map(str, sorted(nums))))


if __name__ == '__main__':
    main()
