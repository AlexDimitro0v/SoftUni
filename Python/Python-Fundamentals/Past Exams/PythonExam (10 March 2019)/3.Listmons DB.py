class Player:
    db_list = []

    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.db_list.append(self)


def report(command):
    if command == 'score descending':
        for obj in sorted(Player.db_list, key=lambda person: (-sum(person.score), person.name)):
            print(f"{obj.name}: {sum(obj.score)}")
    elif command == 'score ascending':
        for obj in sorted(Player.db_list, key=lambda person: (sum(person.score), person.name)):
            print(f"{obj.name}: {sum(obj.score)}")
    elif command == 'numberOfGames descending':
        for obj in sorted(Player.db_list, key=lambda person: (-len(person.score), person.name)):
            print(f"{obj.name}: {len(obj.score)}")
    elif command == 'numberOfGames ascending':
        for obj in sorted(Player.db_list, key=lambda person: (len(person.score), person.name)):
            print(f"{obj.name}: {len(obj.score)}")


def main():
    data = input()
    while data != 'report':
        name, scores = data.split(' -> ')
        scores = list(map(int, scores.split(', ')))
        Player(name, scores)
        data = input()

    command = input()
    while command != 'end':
        report(command)
        command = input()


if __name__ == '__main__':
    main()
