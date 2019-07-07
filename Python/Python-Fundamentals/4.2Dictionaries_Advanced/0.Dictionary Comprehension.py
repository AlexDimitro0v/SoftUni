# https://www.datacamp.com/community/tutorials/python-dictionary-comprehension
# http://cmdlinetips.com/2018/01/5-examples-using-dict-comprehension/
# https://www.geeksforgeeks.org/python-dictionary-comprehension/
"""
To create a dictionary comprehension, we wrap 3 elements around an opening and closing bracket:
1. A base list
2. What the key should be for each item from the base list
3. What the value should be for each item from the base list
i.e: new_dic = {key:value for i in list}
i.e: dict_variable = {value:key for (key,value) in dictionary.items()}

Why Use Dictionary Comprehension?
Dictionary comprehension is a powerful concept and can be used to substitute/replace (nested) for loops and
lambda functions with map(), filter() and reduce(), ...!
However, not all for loop can be written as a dictionary comprehension but all dictionary comprehension can be written
with a for loop.
"""

# Example1:
nums = [1, 2, 3, 4, 5]
dict_comprehension = {
    str(n): "The corresponding key is: " + str(n) for n in nums
    }

for key, val in dict_comprehension.items():
    print(key, val)
print('-'*25)


# Example2:
# create list of fruits
fruits = ['apple', 'mango', 'banana','cherry']
# dict comprehension to create dict with fruit name as keys
dic_compre = {f: len(f) for f in fruits}  # {'cherry': 6, 'mango': 5, 'apple': 5, 'banana': 6}
print(dic_compre)
print('-'*25)


# Example3 (Alternative to for-loops):
numbers = range(10)
new_dict_comp = {n: n**2 for n in numbers if n % 2 == 0}
"""
This can be rewritten as 
new_dict_for = {}

# Add values to `new_dict` using for loop
for n in numbers:
    if n%2==0:
        new_dict_for[n] = n**2

print(new_dict_for)
"""
print(new_dict_comp)
print('-'*25)

# _____________________________________________________________________________________________________________________
# Example4 (Alternative to lambda functions):
# Initialize the `fahrenheit` dictionary
fahrenheit = {'t1': -30, 't2': -20, 't3': -10, 't4': 0}

# Get the corresponding `celsius` values and create the new dictionary
celsius_dict = {k: (float(5)/9)*(v-32) for (k, v) in fahrenheit.items()}

print(celsius_dict)

# _____________________________________________________________
# Instead of writing:
# Initialize `fahrenheit` dictionary
fahrenheit = {'t1': -30, 't2': -20, 't3': -10, 't4': 0}

# Get the corresponding `celsius` values
celsius = list(map(lambda x: (float(5)/9)*(x-32), fahrenheit.values()))

# Create the `celsius` dictionary
celsius_dict = dict(zip(fahrenheit.keys(), celsius))

print(celsius_dict)
print('-'*25)
# _____________________________________________________________________________________________________________________


# Example5 (Multiple Conditions):
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
dict1_doubleCond = {k: v for (k, v) in dict1.items() if v > 2 if v % 2 == 0}
print(dict1_doubleCond)

# Identify odd and even entries
dict1_tripleCond = {k: ('even' if v%2 == 0 else 'odd') for (k, v) in dict1.items()}
print(dict1_tripleCond)
