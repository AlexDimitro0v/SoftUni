class Book:
    bookstore = []
    sold_books = []

    def __init__(self, title, author, chapters, price):
        self.title = title
        self.author = author
        self.chapters = chapters
        self.price = float(price)
        Book.bookstore.append(self)

    def get_chapters_sum(self):
        return len(self.chapters)

    @classmethod
    def request_book(cls, request):
        # Function to sell a book - returns the profit made from the sold book
        dic = {book.title: book for book in cls.bookstore}
        # book = list(filter(lambda b: b.title == request, cls.bookstore))[0]
        if request in dic:
            profit = dic[request].price
            cls.sold_books.append(dic[request])
            return profit
        else:
            print("No such book here")
            return 0


def storing():
    data = input()
    while data != 'on work':
        try:
            book_info, book_chapters = data.split(' -> ')
            title, author, price = book_info.split(' ')
            book_chapters = book_chapters.split(', ')
            if title and author and price and float(price) > 0:
                Book(title, author, book_chapters, price)
            else:
                pass
        except ValueError:
            pass
        data = input()


def main():
    storing()
    requested_book = input()
    profit = 0
    while requested_book != 'end work':
        profit += Book.request_book(requested_book)
        requested_book = input()
    if profit > 0:
        for book in Book.sold_books:
            print(f"SOLD: {book.title} with author {book.author}. "
                  f"Chapters in the book {book.get_chapters_sum()}")
        print(f"Money: {profit:.2f}")
    else:
        print("Bad day :(")


if __name__ == '__main__':
    main()
