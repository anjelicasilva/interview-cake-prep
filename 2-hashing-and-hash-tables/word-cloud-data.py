# Write code that takes a long string and builds its word cloud data in a dictionary ↴ , where the keys are words and the values are the number of times the words occurred.

# My Solution

import string
def word_cloud_data(string_data):

    new_list = []
    for char in string_data:
        if char not in string.punctuation:
            new_list.append(char)
    new_string = "".join(new_list).lower()

    cloud_data = {}

    for word in new_string.split():
        if word.isalpha():
            if word in cloud_data:
                cloud_data[word] += 1
            else:
                cloud_data[word] = 1
    return cloud_data