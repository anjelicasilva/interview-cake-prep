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
 

 # IC Solution

def has_palindrome_permutation(the_string):
    # Track characters we've seen an odd number of times
    unpaired_characters = set()

    for char in the_string:
        if char in unpaired_characters:
            unpaired_characters.remove(char)
        
        else:
            unpaired_characters.add(char)
    
    # The string has a palindrome permutation if it
    # has one or zero characters without a pair
    return len(unpaired_characters) <= 1