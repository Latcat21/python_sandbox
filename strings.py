# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Brian'
age = 34

# Concatenate
# print('Hello I am ' + name + 'and I am ' + str(age))

# String Formatting

# Arguments by name
# print('My name is {name} and i am {age}'.format(name='brian', age='34'))

# F-Strings (only in 3.6+)
# print(f'My name is {name} and I am {age}')

# String Methods
s = 'hello there world'

# Capitalize first letter
print(s.capitalize())

# Make everything upppercase
print(s.upper())

# Make everything lowercase
print(s.lower())

#  Swap Case
print(s.swapcase())

# Length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into list
print(s.split())

# Find position
print(s.find('r'))

# is all alphaunmeric
print(s.isalnum())

# is all alphabetic
print(s.isalpha())

# is all numeric
print(s.isnumeric())

