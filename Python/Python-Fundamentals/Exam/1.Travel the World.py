def main():
    n = int(input())
    money_per_item = float(input())
    reviews = 0
    for times in range(n):
        data = input()
        if data.isalpha():
            print(f"Reviewing location - {data[::-1]}")
            reviews += 1
        elif data.isdigit():
            word = ''
            for i, j in zip(data[::2], data[1::2]):
                word += str(chr(int(i+j)))
            print(f"Reviewing item - {word}")
            reviews += 1
    print(f"{reviews} reviews have been made this month. Salary: {money_per_item*reviews:.2f}")


if __name__ == '__main__':
    main()
