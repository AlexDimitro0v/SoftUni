import collections


def main():
    my_list = list(map(int, input().split()))
    command_count = 0

    data = input()
    while data != 'exhausted':
        command = data.split()[0]
        command_count += 1

        if my_list:
            if command == 'set':            # set is an unordered data structure
                unique_list = collections.OrderedDict.fromkeys(my_list)
                print(list(unique_list)) if len(my_list) != len(unique_list) else print("It is a set")
            elif command == 'filter':
                filter_by = data.split()[1]
                if filter_by == 'even':
                    new_list = [x for x in my_list if x % 2 == 0]
                    if new_list:
                        print(new_list)
                elif filter_by == 'odd':
                    new_list = [x for x in my_list if x % 2 != 0]
                    if new_list:
                        print(new_list)
            elif command == 'multiply':
                number = data.split()[1]
                # print(list(map(lambda x: x*int(number), my_list)))
                print([x*int(number) for x in my_list])
            elif command == 'divide':
                number = data.split()[1]
                try:
                    print([x/int(number) for x in my_list])
                except ZeroDivisionError:
                    print('ZeroDivisionError caught')
            elif command == 'slice':
                index1 = int(data.split()[1])
                index2 = int(data.split()[2])
                if 0 <= index1 < len(my_list)-1 and 0 <= index2 < len(my_list)-1:
                    print(my_list[index1:index2+1])
                else:
                    print('IndexError caught')

            elif command == 'sort':
                print(sorted(my_list))
            elif command == 'reverse':
                print(list(reversed(my_list)))
        else:
            pass
        data = input()
    print(f"I beat It for {command_count} rounds!")


if __name__ == '__main__':
    main()
