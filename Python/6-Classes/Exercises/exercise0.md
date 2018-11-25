# Exercise 0: Vehicle Practice
Create a class called Vehicle.
It will have the attributes: name, type, colour, and value.
It will have a method (aka function) within it called description that will use the vehicle's attributes to create a description.
Make 2 instances of the class or individual vehicle models.
Here is an example of each attribute for an instance of the Vehicle class

```Python
vehicle_1 = Vehicle("Lamborghini Aventador, "car", "black", "$375,000")
print(vehicle_1.description())
```

# Example Output:

```
The Lamborghini Aventador is a black car worth #375,000.
```
To make this description use the format method shown below.

```Python
description_string = "The {} is a {} {} worth {}.".format(self.name, self.colour, self.type, self.value)
```
