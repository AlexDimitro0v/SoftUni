class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        is_one_name = True if len(author.split()) == 1 else False
        if not is_one_name:
            s_name_letter = author.split()[1][0]
            if s_name_letter.isdigit():
                raise Exception("Author not valid!")
        self._author = author

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if len(title) < 3:
            raise Exception("Title not valid!")
        self._title = title

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price <= 0:
            raise Exception("Price not valid!")
        self._price = price

    def __str__(self):
        return f"Type: {self.__class__.__name__}\nTitle: {self.title}\nAuthor: {self.author}\nPrice: {self.price:.2f}\n"


class GoldenEditionBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title, author, price)
        self.price += self.price * 0.3


def main():
    author = input()
    title = input()
    price = float(input())
    try:
        book = Book(title, author, price)
        golden_book = GoldenEditionBook(title, author, price)
        print(book)
        print(golden_book)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
