class Person():
    """
    The Person class has the properties age and name
    self represents the instance of the class.

    The instantiation operation (“calling” a class object) creates an
    empty object. Many classes like to create objects with instances
    customized to a specific initial state. Therefore a class may define
    a special method named __init__(), like this:
    """
    def __init__(self, age,name):
        self.age = age
        self.name = name
    def change_age(self):
        self.age += 1
        return self.age

class Dog(Person):
    """
    The Dog class takes in the Person class and all its functions and properties.
    The change_age method is overidden by the dog's version of that method.
    """
    def change_age(self):
        self.age += 7
        return self.age
"""
Adam and Sean are both 17, but one is a human and the other is a dog
age, name, and dog_name are all variables
"""
age = 17
name = "Adam" 
dog_name = "Sean"

"""
adam is an instance of the Person class
sean is an instance of the Dog class
"""
adam = Person(age,name)
sean = Dog(age,dog_name)
"""
Deeper explanation (using sean):
    The above creates an instance of the class and assigns the object
    the local variable age and dog_name.
    When a class defines an __init__() method, class instantiation
    automatically invokes __init__() for the newly-created class instance.
    A newly initialized instance is shown above.
    All the arguments are passed to the __init__() method.
"""


print(adam.age)
print(adam.name)

print(adam.change_age())
print(sean.change_age())
"""
Lots of things in Python use dictionaries behind the hood
Class instances are one of those
"""
print(adam.__dict__)
