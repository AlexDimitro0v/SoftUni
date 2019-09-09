# https://realpython.com/python-data-types/#built-in-functions      DATA TYPES AND Built-In functions
# https://treyhunner.com/2019/05/python-builtins-worth-learning/    BUILT-INS WORTH-KNOWING

# Python Built-In for solving problems:
# Things I should memorize such that I know them well
# Things I should know about so I can look them up more effectively later
# Things I shouldn’t bother with at all until/unless I need them one day
"""
The commonly known built-in functions (which you likely already know about):
print
len
str
int
float
list
tuple
dict
set
range


The built-in functions which are often overlooked by newer Python programmers:
sum
enumerate
zip
bool
reversed
sorted
min
max
any
all

There are also 5 commonly overlooked built-ins that make debugging easier:
dir, vars, breakpoint, type, help.
"""

# Locals and Globals and Vars()
# https://stackoverflow.com/questions/7969949/whats-the-difference-between-globals-locals-and-vars
"""
1. globals() always returns the dictionary of the module namespace
2. locals() always returns a dictionary of the current namespace
3. vars() returns either a dictionary of the current namespace (if called with no argument) 
   or the dictionary of the argument.
"""

# If you ever try to use my_object.__dict__, you can use vars instead.
# The vars function is sort of a mashup of two related things: checking locals() and testing
# the __dict__ attribute of objects.

# https://www.youtube.com/watch?v=BVXv0-1Rcc8&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=8 USING THE PYTHON TERMINAL
# dir will call all the available modules for you

