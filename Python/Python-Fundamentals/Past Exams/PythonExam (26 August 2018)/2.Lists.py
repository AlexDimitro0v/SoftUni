def main():
    data = input()
    while data != 'stop playing':
        my_list = list(map(int, data.split()))
        if len(set(my_list)) == len(my_list):
            my_list = [x+2 if x % 2 == 0 else x for x in my_list]
            # my_list = list(map(lambda x: x+2 if x % 2 == 0 else x, my_list))
            my_list.sort()
            print(f"Unique list: {','.join(map(str, my_list))}")
            print(f"Output: {sum(my_list)/len(my_list):.2f}")
        else:
            my_list = sorted(list(map(lambda x: x+3 if x % 2 == 1 else x, my_list)))
            print(f"Non-unique list: {':'.join(map(str, my_list))}")
            print(f"Output: {sum(my_list)/len(my_list):.2f}")
        data = input()


if __name__ == '__main__':
    main()
