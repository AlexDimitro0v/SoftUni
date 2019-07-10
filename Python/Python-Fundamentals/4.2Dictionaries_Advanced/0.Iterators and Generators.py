# https://treyhunner.com/2016/12/python-iterator-protocol-how-for-loops-work/   - A MUST FROM Trey Hunner
# https://www.dataquest.io/blog/python-generators-tutorial/
# https://anandology.com/python-practice-book/iterators.html
# https://medium.com/learning-better-ways-of-interpretting-and-using/python-generators-memory-efficient-programming-tool-41f09077353c
# https://www.youtube.com/watch?v=bD05uGo_sVI  - MUST SEE FROM Corey Schafer
# https://opensource.com/article/18/3/loop-better-deeper-look-iteration-python  - COMMON LOOPING GOTCHAS
# https://treyhunner.com/2018/06/how-to-make-an-iterator-in-python/             - THE BEST TO MAKE AN ITERATOR

# Loop like a native   https://www.youtube.com/watch?v=EnSu9hHGq5o
# Loop better          https://www.youtube.com/watch?v=JYuE8ZiDPl4&feature=youtu.be  Trey Hunner
# https://www.youtube.com/watch?v=jTYiNjvnHZY - Iterators and Iterables

# Iterable is any object that can support iteration - i.e can be looped over
# Iterator describes 2 things:
# 1. What item comes next in the iteration.     next()
# 2. When should the loop stop iteration.
# NOTE: Iterable is not necessary an iterator
# NOTE: Iterators are iterables - can be looped over            - SEE COREY VIDEO

my_list = [1, 2, 3, 4, 5]
# print(next(my_list))  TypeError - list is an iterable but not an iterator
print(*my_list)
print(*my_list)     # An iterable can be looped over multiple times

# https://www.freecodecamp.org/news/how-and-why-you-should-use-python-generators-f6fb56650888/ WHY AND HOW?
nums = [1, 2, 3]
i_nums = iter(nums)     # same as i_nums = nums.__iter__()  a.c.a turning the list into iterator
print(next(i_nums))     # could be rewritten with a for loop
print(next(i_nums))
print(next(i_nums))
# print(next(i_nums))   # StopIteration exception

print('-'*25)
# For loops know where to stop without the exception, so they basically do this under the hood:
i_nums2 = iter(nums)
while True:
    try:
        print(next(i_nums2))
    except StopIteration:
        break
print('-'*25)


# Simulating an iterator and an iterable
class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):                     # For something to be an iterable it has to have a __iter__() method
        return self

    def __next__(self):
        if self.value >= self.end:          # For something to be an iterator it has to have a next() method
            raise StopIteration
        current = self.value
        self.value += 1
        return current


my_range = MyRange(1, 10)
for num in my_range:
    print(num)
print('-'*25)


# ______________________________________________________________________________________________________________________
# Generators are iterators themselves
# Generator function is a simpler way to create a generator
def generator_a():
    yield "a"           # If there are no more elements, it raises a StopIteration.


print(next(generator_a()))


def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1


num_list = my_range(1, 10)
for num in num_list:
    print(num)

print('-'*25)

my_nums = (x*x for x in [1, 2, 3, 4, 5])  # generator expression returns a generator (look-alike the list comprehension)
print(*my_nums)
print(sum(my_nums))         # A generator/iterator cannot be looped over multiple times


# https://data-flair.training/blogs/python-generator-vs-iterator/ Python iterator is more memory-efficient than the
# Python generator


"""
# https://stackoverflow.com/questions/2776829/difference-between-pythons-generators-and-iterators
In summary: 
Iterables are objects that can be looped through/over.
Iterators are objects that have an __iter__ and a __next__  method. 
Generators provide an easy, built-in way to create instances of Iterators.
"""
# Note: Both enumerate and zip return iterators to us.

import itertools
print(dir(itertools))       # A closer look to all available itertools methods
# _______________________________________________________________________________________________


# Remove all for loops
def print_each(iterable):
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
        except StopIteration:
            break  # Iterator exhausted: stop the loop
        else:
            print(item)
