# Write an efficient function that tells us whether or not an input string's openers and closers are properly nested.

# My Attempt

def is_valid(code):

    closers = []

    for char in code:
        if char == "(":
            closers.append(")")
        elif char == "{":
            closers.append("}")
        elif char == "[":
            closers.append("]")

        else:
            check_match = closers.pop()
            if char != check_match:
                return False
    return len(closers) == 0