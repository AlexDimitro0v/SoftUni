class Website:
    websites_list = []

    def __init__(self, host, domain, queries=None):
        self.host = host
        self.domain = domain
        if queries:
            self.queries = queries.split(',')
        else:
            self.queries = queries
        self.websites_list += [self]

    def __str__(self):
        if self.queries:
            return f"https://www.{self.host}.{self.domain}/query?=[{']&['.join(self.queries)}]"
            # string]&[string]&[string
        else:
            return f"https://www.{self.host}.{self.domain}"


def no_oop_solution():
    separator = "&"
    data = input()
    while data != 'end':
        data = input().split(" | ")
        host = data[0]
        domain = data[1]
        try:
            queries = data[2].split(",")
            queries = map(lambda x: f"[{x}]", queries)
            print(f"https://www.{host}.{domain}/query?={separator.join(queries)}")
        except IndexError:
            print(f"https://www.{host}.{domain}")

        data = input()


def main():
    data = input()
    while data != 'end':
        Website(*data.split(' | '))
        data = input()

    for obj in Website.websites_list:
        print(obj)                          # Note: the __str__ method is being called


if __name__ == '__main__':
    main()
