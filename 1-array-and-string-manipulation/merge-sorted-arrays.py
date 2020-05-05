# Each order is represented by an "order id" (an integer).
# We have our lists of orders sorted numerically already, in lists. Write a function to merge our lists of orders into one sorted list.


# My Solution

my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

def merge_lists(my_list, alices_list):
    merged_list = []

    while len(my_list) != 0 and len(alices_list) != 0:
        if my_list[0] < alices_list[0]:
            start = my_list.pop(0)
        else: 
            start = alices_list.pop(0)
        merged_list.append(start)

    if len(my_list) == 0 and len(alices_list) != 0:
        merged_list.extend(alices_list)
    else:
        merge_lists.extend(my_list)
    return merged_list

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
print(merge_lists(my_list, alices_list))