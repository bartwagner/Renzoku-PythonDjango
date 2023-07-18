# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'
    def has_birthday(self):
        self.age +=1

class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    def set_balance(self, balance):
        self.balance = balance
    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and I owe a balance of {self.balance}'

# Init user object
brad = User('Brad Traversy', 'brad@gmail.com', 37)
janet = User('Janet Williams', 'janet@gmail.com', 27)
print('Brad:', brad.name)
print('Brad:', brad.age)
print('Brad:', brad.email)

print('Janet:', janet.name)
print('Janet:', janet.age)
print('Janet:', janet.email)

# Edit property
brad.age = 38
print(brad.age)

# Birthday before call greeting
janet.has_birthday()

# Call method
print(janet.greeting())

# Init customer
john = Customer('John Doe','john@gmail.com',40)
john.set_balance(500)

print('John:', john.name)
print('John:', john.balance)
print(john.greeting())