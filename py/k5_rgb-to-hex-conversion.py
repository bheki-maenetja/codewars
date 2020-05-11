# Description:
# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

# The following are examples of expected output values:

# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3

# SOLUTION
def rgb(r, g, b):
    my_list = ['00' if x < 0 else 'FF' if x > 255 else hex(x).split('x')[-1].upper() for x in (r,g,b)]
    my_list = [f'0{x}' if len(x) < 2 else x for x in my_list]
    return ''.join(my_list)