from itertools import permutations as get_perms
# Description:

# In this kata you have to create all permutations of an input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.

# Examples:

# permutations('a'); # ['a']
# permutations('ab'); # ['ab', 'ba']
# permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
# The order of the permutations doesn't matter.

# SOLUTION
def permutations(string):
  rand_strings = list(get_perms(string, len(string)))
  return list(set([''.join(tup) for tup in rand_strings]))

# Example
my_string = input("Enter a string: ")
print('All combinations: ', permutations(my_string))