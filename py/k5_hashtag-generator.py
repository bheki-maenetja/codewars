# Description:
# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!

# Here's the deal:

# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.
# Examples
# " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
# "    Hello     World   "                  =>  "#HelloWorld"
# ""                                        =>  false

# SOLUTION
def generate_hashtag(s):
  hashtag_string = ''.join([word.title() for word in s.split(' ')])
  if len(hashtag_string) > 140 or hashtag_string == '': return False
  return '#{}'.format(hashtag_string)