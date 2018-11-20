class person():
    """
    person has properties age and name
    """
    def __init__(self, age,name):
        self.age = age
        self.name = name
    def change_age():
        self.age += 1
        return self.age

class new_person(person):
    """
    new_person takes in person and all its functions and properties.
    change_age function is overidden by the new_person version
    """
    def change_age():
        self.age += 2
        return self.age

age = 17
name = "Adam"    
new_name = "Sean"

adam = person(age,name)
sean = new_person(age,name)

print(adam.age)
print(adam.name)

print(adam.change_age)
print(sean.change_age)
