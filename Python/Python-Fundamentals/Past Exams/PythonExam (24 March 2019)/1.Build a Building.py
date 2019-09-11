def main():
    money_needed = float(input())
    initial_capital = float(input())
    for times in range(int(input())):
        money = float(input())
        print(f"Investor {times+1} gave us {money:.2f}.")
        initial_capital += money
        if initial_capital >= money_needed:
            print(f"We will manage to build it. Start now! Extra money - {initial_capital-money_needed:.2f}.")
            return

    print(f"Project can not start. We need {money_needed-initial_capital:.2f} more.")


if __name__ == '__main__':
    main()
