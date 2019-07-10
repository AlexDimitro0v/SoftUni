# https://thispointer.com/python-check-if-a-list-contains-all-the-elements-of-another-list/
# https://www.geeksforgeeks.org/python-check-values-list-greater-given-value/
# https://treyhunner.com/2016/11/check-whether-all-items-match-a-condition-in-python/   - MUST SEE


# Python function to check if all values in the list are greater than val using all() function
def check(list1, val):
    return all(x > val for x in list1)


# Checks if a list contains all the elements of another list
def contained(lst1, lst2):
    return all(elem in lst1 for elem in lst2)


def is_prime(candidate):
    divisibility = (
      candidate % n != 0
      for n in range(2, candidate)
    )
    return all(divisibility)


# which is equivalent to:
def is_prime2(candidate):
    return not any(
        candidate % n == 0
        for n in range(2, candidate)
    )


# Quick note: any(item == 'something' for item in iterable) is the same as 'something' in iterable.
# Don’t use all/any for checking containment, use in.
