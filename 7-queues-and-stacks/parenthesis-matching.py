# Write a function that, given a sentence like the one above, along with the position of an opening parenthesis, finds the corresponding closing parenthesis.

# My Attempt
def get_closing_paren(sentence, opening_paren_index):

    parenthesis_counter = 0

    for idx in range(opening_paren_index, len(sentence)):
        if sentence[idx] == "(":
            parenthesis_counter += 1
        elif sentence[idx] == ")":
            parenthesis_counter -= 1
        if parenthesis_counter == 0:
            return idx


 
