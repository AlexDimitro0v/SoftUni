# https://medium.com/understand-the-python/understanding-the-asterisk-of-python-8b9daaa4a558
# https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/


# A function that shows the results of running competitions consisting of 2 to 4 runners.
def save_ranking(first, second, third=None, fourth=None):
    rank = dict()
    rank[1], rank[2] = first, second
    rank[3] = third if third is not None else 'Nobody'
    rank[4] = fourth if fourth is not None else 'Nobody'
    print(rank)


# Pass the 2 positional arguments
save_ranking('ming', 'alice')
# Pass the 2 positional arguments and 1 keyword argument
save_ranking('alice', 'ming', third='mike')
# Pass the 2 positional arguments and 2 keyword arguments (But, one of them was passed as like positional argument)
save_ranking('alice', 'ming', 'mike', fourth='jim')


def save_ranking(*args, **kwargs):
    print(args)     # positional arguments
    print(kwargs)   # keyword arguments


save_ranking('ming', 'alice', 'tom', 'wilson', 'roy', first='ming', second='alice', fourth='wilson', third='tom')
# ('ming', 'alice', 'tom', 'wilson', 'roy')
# {'first': 'ming', 'second': 'alice', 'fourth': 'wilson', 'third': 'tom'}


print('-'*25)
# The Asterisks is also used for unpacking:
numbers = [1, 2, 3, 4, 5, 6]
first, *rest = numbers
print(rest)     # [2, 3, 4, 5, 6]
print(first)    # 1

