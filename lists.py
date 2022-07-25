# A list is a collection which is ordered and changeable. Allows duplicate members.

# create list
numbers = [1,2,3,4,5]

# using a constructor
numbers2 = list((1,2,3,4))

fruits = ['apple', 'oranges', 'Grapes', 'Pears']

# Get value
print(fruits[1])

# get length
print(len(fruits))

# Append to list
fruits.append('grapes')

# Remove from list
fruits.remove('Grapes')

# Insert into position
fruits.insert(2, 'Strawberryies')

# Remove from position
fruits.pop(3)

# Reverse
fruits.reverse()

# Sort list
fruits.sort()

# reverse Sort
fruits.sort(reverse=True)


print(fruits)
