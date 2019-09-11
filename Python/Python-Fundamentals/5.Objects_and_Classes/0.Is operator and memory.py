# https://www.geeksforgeeks.org/difference-operator-python/
list1 = []
list2 = []
list3 = list1

print(list1 == list2)       # True  - both are empty lists
print(list1 is list2)       # False - different memory locations
print(list1 is list3)       # True  - both lists are pointing to the same object - pointing to the same memory location
print(id(list1), id(list2), id(list3))
"""
When assigning a name of a variable in Python, you: 
1.Create a PyObject
2.Set the typecode to integer for the PyObject
3.Set the value to 2337 for the PyObject
4.Create a name called x
5.Point x to the new PyObject

Meaning that there are no exact pointers in Python
https://realpython.com/pointers-in-python/   -> More Info here
# Remember that in Python, names are just labels referencing values !!!!!!!!!!!!!!!!!!!!!!!!!!!
"""

print('-'*25)
a = 1
b = 1
c = a

print(a == b)       # True  - both have value of 1
print(a is b)       # True  - same memory locations, both variable names point to the same memory location now
print(a is c)       # True  - both variables are pointing to the same object
c += 1
print(id(a), id(b), id(c))      # because of the last line c has a different memory address now


print('-'*25)
a = [1, 2]
b = [3, 4]
a = b                           # Now a = [3, 4] and has the same id as b
print(id(a), id(b))             # is operator returns True
b = [5]                         # b is reassigned to a new list and occupies a new memory location
print(a)

# Conclusion:
# The 'is' operator tests:
#      if two variables point to the same memory location, i.e
#      if two variables point the same object, not if two variables have the same value.
#      if two variables have the same id
# Note: When variables point to the same object, the changes in 1 of the variables are reflected to the other as well.

# The == operator tests:
#      if variables have the same value

# Remember that in Python, names are just labels referencing values
