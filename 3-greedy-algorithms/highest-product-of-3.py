# Given a list of integers, find the highest product you can get from three of the integers.

# The input list_of_ints will always have at least three integers.


# My Attempt
def highest_product_of_3(list_of_ints):

    # Calculate the highest product of three numbers

    if len(list_of_ints) < 3:
        raise ValueError("Need at least 3 integers")

    first = list_of_ints[0]
    second = list_of_ints[1]
    third = list_of_ints[2]

    for num in range(3, len(list_of_ints)):
        if num > first:
            first = num
        elif num > second:
            second = num
        elif num > third:
            third = num
    return first * second * num