# https://www.dataquest.io/blog/tutorial-functions-modify-lists-dictionaries-python/ - MUST SEE
# https://medium.com/@meghamohan/mutable-and-immutable-side-of-python-c2145cf72747   - Very helpful
# https://realpython.com/pointers-in-python/ - MUST SEE


# Immutable objects(Float, Int, String):
def fun(x, y, z):
    x = z - y
    y = z - 1
    print(x, y, z)


a = 2
b = 4
c = 8
fun(a, b, b + c)
print(a, b, c)          # The initial values of a, b and c are unchanged


print('-'*25)
a = 5
# print(id(a))
b = 6

b = a
a += 1              # Now a occupy a different address in the memory
# print(id(a))
print('а =', a)
print('b =', b)     # B is unchanged


# _______________________________________________________________________________________________
# Mutable objects(Lists, Dictionaries):
my_list_1 = [1, 2, 3]
my_list_2 = [4, 5, 6]
# print(id(my_list_1), id(my_list_2))   different id's

my_list_1 = my_list_2    # list2 is assigned to list1
my_list_2[0] = 100       # changing the value of the 1st element in the list

print(my_list_1)
print(my_list_2)         # both lists are changed, because they are mutable and occupy the same address in the memory
# print(id(my_list_1), id(my_list_2))   same id's


initial_list = [1, 2, 3]


def duplicate_last(a_list):
    last_element = a_list[-1]
    a_list.append(last_element)
    return a_list


new_list = duplicate_last(a_list=initial_list)
print(new_list)      # [1, 2, 3, 3]
print(initial_list)  # [1, 2, 3, 3]
