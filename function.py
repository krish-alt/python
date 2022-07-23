# length function

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(list))

# sum function
print(sum(list))


def sum_list(list):

    """add all the elements in the list"""
    sum = 0
    for i in list:
        sum += i
    return sum

help(sum_list)    

# help on function sum_list in module __main__:sum_list(list) sum of the list elements 