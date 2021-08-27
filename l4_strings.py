name = 'Jennifer'

print('nth char: ' + name[1])
print('nth last char: ' + name[-1])
print('from nth-index till mth (mth excluded): ' + name[0:4])
print('until the nth char (assuming starting from 0): ' + name[: 5])
print('from nth-index till the end: ' + name[3:])
print('copy string: ' + name[:])

# ----------------------------------------

multi_line_string = '''
Hi John,

Thank you for your email.
We will try to get to you ASAP.

Have a great day.


Best Regards,
Antwan
'''

print(multi_line_string)

# ----------------------------------------

first_name = 'John'
last_name = 'Doe'

message = first_name + ' [' + last_name + '] is a programmer';
print(message)

formatted_message = f'{first_name} [{last_name}] is a programmer'
print(formatted_message)
