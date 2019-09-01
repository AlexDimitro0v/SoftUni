# https://stackoverflow.com/questions/3620943/measuring-elapsed-time-with-the-time-module?import sys
import sys
import timeit

data = (int(e) for e in ['4']*100)
data2 = [int(e) for e in ['4']*100]
data3 = map(int, ['4']*100)
print(sys.getsizeof(data))
print(sys.getsizeof(data2))
print(sys.getsizeof(data3))

# you can use a for loop and try both of them with 10000 times or more, you will notice that the map function
# is quicker than the list one.
# ex:
x = timeit.timeit("[str(i) for i in range(100)]", number=10000)
print(x)

y = timeit.timeit("map(str, range(100))", number=10000)
print(y)


"""
# https://stackoverflow.com/questions/1247486/list-comprehension-vs-map?rq=1
(map) may be microscopically faster in some cases (when you're NOT making a lambda for the purpose, but using the same 
function in map and a listcompr).
(List comprehensions) may be faster in other cases and most (not all) pythonistas consider them more direct and clearer.
"""

# print(help(memoryview))
print(help(sys.getsizeof))

# https://stackoverflow.com/questions/14650495/difference-between-timeit-and-time-in-python     timeit and time
# https://stackoverflow.com/questions/3620943/measuring-elapsed-time-with-the-time-module?      time measurements
