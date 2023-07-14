# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
# Using a constructor
numbers = [1,2,3,4,5]
numbs = list((1,2,3,4,5))
fruits = ['Apples','Oranges','Grapes','Pears', 12]

# Get value
print(type(numbers))
print(numbers)
print(numbs)
print(fruits)
print(fruits[1])

# Get len
print(len(fruits))

# Append to list
fruits.append('Mangos')
print(fruits)

# Remove from list
fruits.remove(12)
print(fruits)

# Insert into position
fruits.insert(2, 'Strawberries')
print(fruits)

# Remove from position
fruits.pop(3)
print(fruits)

# Reverse list
fruits.reverse()
print(fruits)

# Sort list
fruits.sort()
print(fruits)

# Reverse sort
fruits.sort(reverse=True)
print(fruits)