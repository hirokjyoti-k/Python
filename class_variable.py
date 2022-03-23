class Person:

    instance_counter = 0 #class variable

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.instance_counter += 1

    @classmethod #class method decorators
    def instance_counter_method(cls):
        return f"You have created {cls.instance_counter} instances of {cls.__name__} class"


p1 = Person("Hirok", 22)
p2 = Person("Kalita", 23)

print(Person.instance_counter_method())