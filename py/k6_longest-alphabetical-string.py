# DESCRIPTION
# Find the longest substring in alphabetical order.

# Example: the longest alphabetical substring in "asdfaaaabbbbcttavvfffffdf" is "aaaabbbbctt".

# There are tests with strings up to 10 000 characters long so your code will need to be efficient.

# The input will only consist of lowercase characters and will be at least one letter long.

# If there are multiple solutions, return the one that appears first.

# Good luck :)

# SOLUTION
def longest(s):
    sub_strings = []
    sub_string = ''
    
    for i in range(len(s)):
        if i == 0:
            sub_string = sub_string + s[i]
        elif ord(s[i]) >= ord(s[i - 1]):
            sub_string = sub_string + s[i]
        else:
            sub_strings.append(sub_string)
            sub_string = s[i]
    sub_strings.append(sub_string)
    return max(sub_strings, key=len)