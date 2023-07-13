# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""
#x = 1            # int
#y = 2.5          # float
#name = 'Brad'    # string
#is_cool = True   # bool

# Multiple assigmnet
x, y, name, is_cool = (1, 2.5, 'Brad', True)
print(x, y, name, is_cool)
print('----------------------')

# Basic math
a = x + y
print(a)
print('----------------------')

# Check type
print(type(x))
print(type(y))
print(type(name))
print(type(is_cool))
print('----------------------')

# Casting
x = str(x)
y = int(y)
z = float(y)

# Check type 
print(type(x))
print(type(y))
print(type(z))
print(x)
print(y)
print(z)
print('----------------------')