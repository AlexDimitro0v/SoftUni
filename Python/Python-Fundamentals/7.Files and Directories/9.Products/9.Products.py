import pickle
active_products = []


class Product:
    def __init__(self, type_, name, price, quantity):
        self.type_ = type_
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def __str__(self):
        return f"{self.name} ({self.type_}: {self.quantity} left) - ${self.price}\n"


def load():
    try:                # try loading the database
        with open('save.pickle', 'rb') as load_file:
            stocked_products = pickle.load(load_file)
            return stocked_products
    except FileNotFoundError:
        return []


def save():
    with open("save.pickle", "wb") as save_file:
        pickle.dump(active_products, save_file)


def main():
    data = input()
    while data != 'exit':
        product_names = [pr.name for pr in active_products]
        try:
            name, type_, price, quantity = data.split()
            if name not in product_names:
                product = Product(type_, name, price, quantity)
                active_products.append(product)
            else:
                try:
                    current_product = list(filter(lambda p: p.name == name and p.type_ == type_, active_products))[0]
                    current_product.price = float(price)
                    current_product.quantity = int(quantity)
                except IndexError:
                    product = Product(name=name, type_=type_, price=price, quantity=quantity)
                    active_products.append(product)
        except ValueError:
            if data == 'stock':
                # Stock the active products list and then empty it
                with open('stocked_products.txt', 'a') as file:
                    if active_products:
                        file.writelines(map(str, active_products))
                save()
                active_products.clear()       # clears the active products
            elif data == 'analyze':
                # All Stocked products must be printed
                stocked_products = load()
                if stocked_products:
                    for p in sorted(stocked_products, key=lambda obj: obj.type_):
                        print(f"{p.type_}, Product: {p.name}\nPrice: ${p.price:.2f}, Amount Left: {p.quantity}")
                else:
                    print("No products stocked")
            elif data == 'sales':
                # Deals only with the active products and not with the stored ones
                groceries = sum(obj.price*obj.quantity for obj in list(filter(lambda pr: pr.type_ == 'Food',
                                                                              active_products)))
                electronics = sum(obj.price*obj.quantity for obj in list(filter(lambda pr: pr.type_ == 'Electronics',
                                                                                active_products)))
                domestics = sum(obj.price*obj.quantity for obj in list(filter(lambda pr: pr.type_ == 'Domestics',
                                                                              active_products)))

                incomes_dic = {}
                if groceries > 0:
                    incomes_dic['Food'] = groceries
                if electronics > 0:
                    incomes_dic['Electronics'] = electronics
                if domestics > 0:
                    incomes_dic['Domestics'] = domestics

                for type_, income in sorted(incomes_dic.items(), key=lambda kvp: -kvp[1]):
                    print(f"{type_}: ${income:.2f}")

        data = input()


if __name__ == '__main__':
    # active_products = load()   the Business logic makes more sense if the active products are not loaded at every run
    main()


"""
SamsungSmartTV Electronics 4000.50 10
Banana Food 1.50 10000
IPhone7 Electronics 1000 100
Apple Food 1 100000
Banana Food 5 555
Apple Electronics 3 333
stock
exit
"""
