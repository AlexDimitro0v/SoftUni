def main():
    my_list = list(map(int, input().split()))
    command_count = 0
    valid_commands = ['swap', 'enumerate_list', 'max', 'min', 'get_divisible']

    data = input()
    while data.split()[0] != 'end':
        command = data.split()[0]
        if command in valid_commands:
            command_count += 1
        if command == 'swap':
            index1 = int(data.split()[1])
            index2 = int(data.split()[2])
            try:
                my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
            except IndexError:
                pass
            print(my_list)
        elif command == 'enumerate_list':
            print(list(enumerate(my_list)))

        elif command == 'max':
            print(max(my_list))
        elif command == 'min':
            print(min(my_list))
        elif command == 'get_divisible':
            number = int(data.split()[2])
            new_list = list(filter(lambda x: x % number == 0, my_list))
            print(new_list)
        data = input()
    print(command_count)


if __name__ == '__main__':
    main()


"""
1 3 2 4 5
enumerate_list
swap 3 2
end
"""
