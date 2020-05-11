# Description:
# Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

# The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

# It is much easier to understand with an example:

# format_duration(62) returns "1 minute and 2 seconds"
# format_duration(3662) returns "1 hour, 1 minute and 2 seconds"
# For the purpose of this Kata, a year is 365 days and a day is 24 hours.

# Note that spaces are important.

# Detailed rules
# The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

# The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

# A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

# Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

# A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

# A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.

# SOLUTION
def format_duration(seconds):
    years, nibble = seconds // (365 * 86400), seconds/(365 * 86400) - seconds//(365 * 86400)
    days, nibble = int(nibble * 365), nibble * 365 - int(nibble * 365)
    hours, nibble = int(nibble * 24), nibble * 24 - int(nibble * 24)
    minutes, nibble = int(nibble * 60), nibble * 60 - int(nibble * 60)
    seconds = round(nibble * 60)
    if seconds == 60:
        seconds = 0
        minutes += 1
    
    my_list = []
    
    time_periods = [(years, 'year'), (days, 'day'), (hours, 'hour'), (minutes, 'minute'), (seconds, 'second')]
    
    for i in time_periods:
        format_string = '' if i[0] == 0 else str(i[0])
        if i[0] > 0: format_string = f'{i[0]} {i[1]}s' if i[0] > 1 else f'{i[0]} {i[1]}'
        if format_string != '': my_list.append(format_string)
    
    if len(my_list) == 0: return 'now'
    return_string = my_list[0] if len(my_list) == 1 else ', '.join(my_list[:-1]) + f' and {my_list[-1]}'
    return return_string