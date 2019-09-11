class DBHelper:
    # database_dic = {}

    def __init__(self, location, available_flats=0, price='None'):
        self.location = location
        self.available_flats = available_flats
        self.price = price
        # DB.database_dic[self.neighborhood] += self.block_numbers


def research():
    database_dic = {}
    data = input()
    while data != 'collectApartments':
        neighborhood, block_numbers = data.split()[0], list(map(int, data.split()[2].split(',')))
        database = DBHelper(neighborhood)
        if neighborhood not in database_dic:
            database_dic[neighborhood] = {}
        for bl_number in block_numbers:
            database_dic[database.location][bl_number] = [database.available_flats, database.price]
        data = input()
    return database_dic


def report(database_dic):
    data = input()
    while data != "report":
        info1, info2 = data.split()[0], data.split()[2]
        neighborhood, block_number = info1.split('&')
        available_flats, price = info2.split('|')
        if neighborhood in database_dic.keys():
            if int(block_number) in database_dic[neighborhood].keys():
                database_dic[neighborhood][int(block_number)] = [int(available_flats), int(price)]
        data = input()

    return database_dic


def main():
    database_dic = research()
    report_dic = report(database_dic)
    ordered_neighborhood = dict(sorted(report_dic.items(), key=lambda x: x[0]))
    for neigbourhood, data in ordered_neighborhood.items():
        print(f"Neighborhood: {neigbourhood}")
        for key, value in sorted(data.items(), key=lambda x: x[0]):
            print(f"* Block number: {key} -> {value[0]} apartments for sale. Price for one: {value[1]}")


if __name__ == '__main__':
    main()


"""
Lozenec -> 11,2
Durvenica -> 4,3
Mladost1 -> 5,2
Mladost2 -> 7,8
collectApartments
Lozenec&11 -> 2|100000
Lozenec&2 -> 1|100000
Durvenica&3 -> 5|80000
Durvenica&5 -> 15|80000
Mladost2&13 -> 6|80000
Mladost1&13 -> 7|79000
report
"""
