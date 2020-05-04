# Write a function reverse_words() that takes a message as a list of characters and reverses the order of the words in place
# For example:
    # message = [ 'c', 'a', 'k', 'e', ' ',
    #             'p', 'o', 'u', 'n', 'd', ' ',
    #             's', 't', 'e', 'a', 'l' ]

    # reverse_words(message)

# # Prints: 'steal pound cake'
# print(''.join(message))



# My Solution
def reverse_words(message):
    left_index = 0
    right_index = len(message)-1
    while left_index < right_index:
        message[left_index], message[right_index] = message[right_index], message[left_index]
        left_index += 1
        right_index -= 1

    start_index = 0

    for idx, char in enumerate(message):
        if char == ' ' or idx == len(message) - 1:
            if idx == len(message) - 1:
                end_idx = idx
            else: 
                end_idx = idx - 1

            while start_index < end_idx:
                message[start_index], message[end_idx] = message[end_idx], message[start_index]
                start_index += 1
                end_idx -= 1

            start_index = idx + 1

reverse_words(message)
print(''.join(message))
