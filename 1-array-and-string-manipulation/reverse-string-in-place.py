# Write a function that takes a list of characters and reverses the letters in place

letters = ['a', 'b', 'c', 'd', 'e']

def reverse(letters):
    start = 0
    end = len(letters)-1

    while start < end:
        holder = letters[start]
        letters[start] = letters[end]
        letters[end] = holder
        start += 1
        end -= 1
    return letters

print(reverse(letters))