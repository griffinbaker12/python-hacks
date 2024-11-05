import logging

logging.basicConfig(level=logging.INFO)


class Random:
    def __set_name__(self, owner, name):
        logging.info("assigned to %r", name)


class LoggedAgeAccess:
    # so I am guessing that this gets called when you create an instance of this class
    # and assign it to a variable?

    def __set_name__(self, owner, name):
        # you are setting these on the descriptor itself!
        self.public_name = name
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        value = getattr(obj, self.private_name)
        logging.info("Accessing %r results in %r", "age", value)
        return value

    def __set__(self, obj, value):
        logging.info("Updating %r to %r", self.public_name, value)
        setattr(obj, self.private_name, value)


class Person:
    # get stored as a class variable
    # and then can see the name of what it gets assigned to (happens when the class is defined, not for each instance)
    # the class can inform each descriptor about which variable name was used
    age = LoggedAgeAccess()  # Descriptor instance (created when the class is defined)
    random = Random()

    def __init__(self, age):
        self.age = age

    def birthday(self):
        self.age += 1

    @property
    def method(self):
        return f"The age is {self.age}"

    # def __init__(self, name, age):
    #     self.name = name  # Regular instance attribute
    #     print(id(self), "id of self")
    #     self.age = age  # Calls __set__()...triggers descriptor!!!
    #
    # def birthday(self):
    #     self.age += 1


p = Person(10)
print(p, vars(p), vars(Person))
print(p.age)

p.birthday()
print(p.method)
