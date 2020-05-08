# Write an efficient function that checks whether any permutation 
# of an input string is a palindrome.

# You can assume the input string only contains lowercase letters.

# Examples:
#     "civic" should return True
#     "ivicc" should return True
#     "civil" should return False
#     "livci" should return False

def is_palindrome(input_string):
    letter_dict = {}
    for char in input_string:
        if char not in letter_dict:
            letter_dict[char] = 1
        else:
            letter_dict[char] += 1

    odd_count = 0

    for value in letter_dict.values():
        if value % 2 != 0:
            odd_count += 1
        if odd_count > 1:
            return False
    return True
