import logging
import os

logging.basicConfig(level=logging.INFO)


class T:
    def f(self): ...


t = T()


# When you access the method of an instance, the function does not exist on the instance
print(t.__dict__)  # {}...empty dict!

# When you do access the method...
t.f()  # <function T.f at 0x1007f4c20>

# Can't find 'f' in the __dict__ of the instance, so we look to the class (Pizza.__dict__)

print(
    T.__dict__["f"], "class dict", hasattr(T.__dict__["f"], "__get__")
)  # function in the class dict is a descriptor
print(T.f.__dict__, "function dict")  # {}
print(
    T.f.__class__, "function object"
)  # has __get__ (not on the instance and is resolved through MRO)
print(hasattr(T.f, "__get__"))  # True

print("bound method", t.f, "underlying function", t.f.__func__)
print(T.f)


class Ten:
    def __get__(self, obj, objtype=None):
        print(f"The obj is: {obj}, and the objtype is {objtype}")
        return 10


class A:
    x = 5
    y = Ten()


a = A()
print(f"a is: {a}")
# 10 gets computed on demand (ie, not stored in the class nor instance dictionary)
print(a.x, a.y)

print("A dict:", A.__dict__)
print("a dict:", a.__dict__)
print("Ten dict:", Ten.__dict__)

print("A.y", a.y, A.__dict__["y"].__class__.__dict__)
y_attr = A.__dict__["y"]
print("y attr:", y_attr, hasattr(y_attr, "__get__"))
print(y_attr.__class__.__get__(a, a))


def test(q, *args, **kwargs):
    print(f"q is {q}")


tup = (1, 2, 3)
test(*tup)


class DirectorySize:
    tag = 1

    # the self is the descriptor instance and is part of the obj
    def __get__(self, obj, objtype=None):
        # self is an instance of DirectorySize
        # obj is an instance of Directory
        print("the self is: ", self, self.tag)
        print("the obj is: ", obj)
        print("the objtype is: ", objtype)
        return len(os.listdir(obj.dirname))


class Directory:
    size = DirectorySize()

    def __init__(self, dirname):
        self.dirname = dirname


s = Directory("songs")
print(s.size)


class LoggedAgeAccess:
    def __set_name__(self, owner, name):
        print("setting name %r on id", (name, id(owner)))
        self.public_name = name
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        value = obj._age
        logging.info("Accessing %r giving %r", "age", value)
        return value

    def __set__(self, obj, value):
        logging.info("Updating %r to %r", "age", value)
        obj._age = value


class Person:
    age = LoggedAgeAccess()  # Descriptor instance (created when the class is defined)

    def __init__(self, name, age):
        self.name = name  # Regular instance attribute
        print(id(self), "id of self")
        self.age = age  # Calls __set__()...triggers descriptor!!!

    def birthday(self):
        self.age += 1


p = Person("joe", 30)
print(type(p), p.__class__)
# print(p.age)

# seems like type() and __class__ do the same thing...so what is the right way to think about this?
# there is a corresponding function to most / all dunder methods?

# and then there is dirs vs var?
print(p.__dict__, vars(p))
print(dir(p))

p.age = 50
print(p.age)
setattr(p, "age", 100)
