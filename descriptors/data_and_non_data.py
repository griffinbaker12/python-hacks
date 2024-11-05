class NonDataDescriptor:
    def __init__(self, value) -> None:
        self.value = value

    def __get__(self, obj, owner):
        return self.value


class DataDescriptor:
    def __init__(self, value) -> None:
        self.value = value

    def __get__(self, obj, owner):
        return self.value

    def __set__(self, obj, value):
        self.value = value


class Person:
    non_data = NonDataDescriptor("default")
    data = DataDescriptor("default")


p = Person()

# initial state
print("Initial values:")
print(p.non_data)
print(p.data)

# set values on the instance directory
print("\nSetting values directly on the instance directory:")
p.__dict__["non_data"] = "instance value"
p.__dict__["data"] = "instance value"

# here's where they differ
print("\nAccessing after setting instance attributes:")
print(p.non_data)  # dict wins
print(p.data)

print(vars(Person), vars(p))
