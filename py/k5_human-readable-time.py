# Description:
# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

# You can find some examples in the test fixtures.

# SOLUTION
def make_readable(seconds):
    if seconds == 0: return "00:00:00"
    hours, nibble = str(seconds // 3600), seconds/3600 - seconds//3600
    minutes, nibble = str(int(nibble * 60)), nibble * 60 - int(nibble * 60)
    seconds = str(round(nibble * 60))
    my_list = [f'0{x}' if len(x) < 2 else x for x in (hours, minutes, seconds)]
    return ':'.join(my_list)