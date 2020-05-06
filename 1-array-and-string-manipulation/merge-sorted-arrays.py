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




# IC Solution
def merge_lists(my_list, alices_list):
    # Set up our merged_list
    merged_list_size = len(my_list) + len(alices_list)
    merged_list = [None] * merged_list_size

    current_index_alices = 0
    current_index_mine = 0
    current_index_merged = 0
    while current_index_merged < merged_list_size:
        is_my_list_exhausted = current_index_mine >= len(my_list)
        is_alices_list_exhausted = current_index_alices >= len(alices_list)
        if (not is_my_list_exhausted and
                (is_alices_list_exhausted or
                 my_list[current_index_mine] < alices_list[current_index_alices])):
            # Case: next comes from my list
            # My list must not be exhausted, and EITHER:
            # 1) Alice's list IS exhausted, or
            # 2) the current element in my list is less
            #    than the current element in Alice's list
            merged_list[current_index_merged] = my_list[current_index_mine]
            current_index_mine += 1
        else:
            # Case: next comes from Alice's list
            merged_list[current_index_merged] = alices_list[current_index_alices]
            current_index_alices += 1

        current_index_merged += 1

    return merged_list