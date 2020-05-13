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


# IC Solution
def highest_product_of_3(list_of_ints):
    if len(list_of_ints) < 3:
        raise ValueError('Less than 3 items!')

    highest = max(list_of_ints[0], list_of_ints[1])
    lowest = min(list_of_ints[0], list_of_ints[1])
    highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    lowest_product_of_2 = list_of_ints[0] * list_of_ints[1]

    highest_product_of_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    for i in range(2, len(list_of_ints)):
        current = list_of_ints[i]

        highest_product_of_3 = max(highest_product_of_3,
                                current * highest_product_of_2,
                                current * lowest_product_of_2)

        highest_product_of_2 = max(highest_product_of_2,
                                current * highest,
                                current * lowest)

        lowest_product_of_2 = min(lowest_product_of_2,
                                current * highest,
                                current * lowest)

        highest = max(current, highest)

        lowest = min(current, lowest)

    return highest_product_of_3
