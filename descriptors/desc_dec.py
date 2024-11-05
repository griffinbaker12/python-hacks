class UpperCase:
    def __init__(self, fn):
        print("the fn is:", fn)
        self.fn = fn

    def __get__(self, obj, owner):
        if obj is None:  # class access?
            return self
        return self.fn(obj).upper()


class Person:
    def __init__(self, name):
        self._name = name

    # equivalent to:
    # name = UpperCase(name)
    # and then name is a descriptor. __get__ gets invoked when you access
    # one instance of this is created at class definition (like other methods)
    @UpperCase
    def name(self):
        return self._name


p = Person("joe")
print(p.name)
print(Person.name)
