from inspect import signature
from typing import get_type_hints


def test(*args, **kwargs):
    print(args, kwargs)


test(1, 2, 3)


class Test: ...


t = Test()
print(Test.__name__)


def is_admin(f):
    def wrapper(*args, **kwargs):
        """
        I wrap stuff.
        """
        if kwargs.get("username") != "admin":
            raise Exception("This user is not allowed to get food.")
        return f(*args, **kwargs)

    return wrapper


def foobar(username: str = "someone") -> None:
    """
    Do crazy stuff.
    """
    ...


print(foobar.__name__)  # foobar
print(foobar.__qualname__)  # foobar
print(foobar.__annotations__)  # {'username': <class 'str'>, 'return': None}
print(foobar.__doc__)  # Do crazy stuff.

# TODO: assuming that this looks at the annotations dunder?
# foobar(5)


@is_admin
def foobar(username: str = "someone"):
    "Do crazy stuff."
    print("the annotations are", __annotations__)
    ...


print(foobar.__name__)  # wrapper
print(foobar.__qualname__)  # is_admin.<locals>.wrapper
print(foobar.__annotations__)  # {}
print(foobar.__doc__)  # I wrap stuff.

foobar(username="admin")


print(get_type_hints(foobar).get("username") is str)
print("ehy")

sig = signature(foobar)
print("the sig is", sig)

bound = sig.bind()
print(bound.apply_defaults())
print(bound)


class Test: ...


t = Test()

for i in range(5):
    print("i is...", i)
    try:
        v = getattr(t, "name")
    except:
        print("?")
    else:
        print("Uh")
else:
    print("not there")
