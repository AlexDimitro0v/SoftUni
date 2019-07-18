class BankAccount:
    list_accounts = []      # class variable to store all instances of the class

    def __init__(self, bank, name, balance):
        self.name = name
        self.bank = bank
        self.balance = float(balance)
        BankAccount.list_accounts.append(self)


def main():
    data = input()
    while data != 'end':
        BankAccount(*data.split(' | '))
        data = input()

    for acc in sorted(BankAccount.list_accounts, key=lambda obj: (-obj.balance, len(obj.bank))):
        print(f"{acc.name} -> {acc.balance:.2f} ({acc.bank})")


if __name__ == '__main__':
    main()
