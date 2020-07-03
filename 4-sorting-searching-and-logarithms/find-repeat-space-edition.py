# Write a function which finds an integer that appears more than once in our list. (If there are multiple duplicates, you only need to find one of them.)

def find_repeat(numbers):
    numbers_seen = set()
    for number in numbers:
        if number in numbers_seen:
            return number
        else:
            numbers_seen.add(number)

    # Whoops--no duplicate
    raise Exception('no duplicate!')