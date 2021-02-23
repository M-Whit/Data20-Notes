# class Dog:
#     # A variable inside a class is a class variable
#     animal_kind = 'Canine'
#
#     # __init__ Constructor method
#     # Initialisation - Creates instance variables for the class
#     # Instantiation - Creation of an instance of an object
#     # Don't get these two mixed up!
#
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
#         self.bark() # Now the doggy barks when it's made! :D
#
#     # Method, self is a parameter that acts as a reference to the current instance of the class
#     # This method is only available to the class, and is not available on the Global Scope
#     # Inside the class, all parameters are available to the class
#     # Removing self will cause errors, self is used for the print statement to work
#     # Outside the class, this 'self' would be 'Dog'
#
#     # When we use underscores, we can hide things in Python
#     # The class can still use the method, but outside of the class, bark will be hidden
#
#     def bark(self):
#         print(self.animal_kind)
#         print('woof')
#
# # print(Dog.animal_kind)
# #
# # # Methods are only available to class objects, and we haven't yet made an object
# # # print(Dog.bark()) does not work
# #
# # # Create a dog Object
# # # Need to fill in the names and breeds as defined by __init__
#
#
# husky = Dog("husky", "husky")
# lacey = Dog("lacey", "jack russell")
#
# print(type(husky)) # <class '__main__.Dog'>
# print(husky.bark()) # woof
# print(husky.animal_kind) # Canine
#
# # Can change the parameters of individual objects without affecting the overall Class
# husky.animal_kind = 'Big Dog'
# print(husky.animal_kind) # Prints 'Big Dog'
# print(lacey.animal_kind) # Prints 'Canine'
#
# # Only Lacey is affected here
# # If you haven't DIRECTLY specified what an object is, it is affected by a change in Dog.animal_kind
# # Because we previously specified husky was 'Big Dog', it is unaffected by Dog.animal_kind = 'Dolphin'
# Dog.animal_kind = 'Dolphin'
# print(husky.animal_kind) # Prints 'Big Dog'
# print(lacey.animal_kind) # Prints 'Dolphin'
#
# # Can look at other things in each object now
# print(lacey.breed) # 'Jack Russell'
# print(lacey.name) # 'lacey'
#
# class MethodExamples:
#
#     def __init__(self):
#         self._this_can_be_accessed = "I can be accessed easily"
#
#     def get_this_can_be(self):
#         return self._this_can_be_accessed
#
#     def set_this_can_be(self, value_to_be_set):
#         self._this_can_be_accessed = value_to_be_set
#
#
# x = MethodExamples()
#
# print(x.get_this_can_be()) # Prints 'I can be accessed easily'
# class Animal:
#
#     def __init__(self):
#         self.alive = True
#         self.breathe()
#
#     def breathe(self):
#         print("One breath in, One breath out")
#
#
# class LandMammal(Animal):
#
#     def __init__(self, legs):
#         super().__init__()
#         self.legs = legs
#
#     def run(self):
#         return "I can run!"
#
#
# # Inherit breathe method through super(), so our Horse and Mammoth breathe upon creation
# Horse = Animal()
# Mammoth = LandMammal(4)
#
# # We can kill horse
# # Which is one reason why you might want to hide certain methods using dunders (__)
# Horse.alive = False
# print(Horse.alive)
#
# print(Mammoth.run())
