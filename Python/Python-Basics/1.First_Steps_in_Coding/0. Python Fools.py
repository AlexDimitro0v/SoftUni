"""Some Python Fools"""
# https://realpython.com/python-data-types/#built-in-functions      DATA TYPES AND Built-In functions
# https://treyhunner.com/2019/05/python-builtins-worth-learning/    BUILT-INS WORTH-KNOWING
a = ''
b = ' '  # the only value
c = None
d = []
e = 0
# False also has no value -> if condition evaluates to False

print(f"a: {bool(a)}")
print(f"b: {bool(b)}")
print(f"c: {bool(c)}")
print(f"d: {bool(d)}")
print(f"e: {bool(e)}")

if a:  # When you write if variable(no matter which), the check will tell you if it exists or it is True
    print("print a ", a)

if b:
    print("print b ", b)

if c:
    print("print c ", c)

if d:
    print("print d ", d)

if e:
    print("print e ", e)

randomList = [1, 'a', 0, True, False, '', '0']
filteredList = list(filter(None, randomList))           # should be casted to a list!
print('The filtered elements are:', filteredList)       # Contains only the True values (the None values are filtered)

# When we loop through the final filteredList, we get the elements which are true: 1, a, True and '0'
# ('0' as a string is also true).
