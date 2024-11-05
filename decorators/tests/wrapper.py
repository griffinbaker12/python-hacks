import inspect
from functools import partial

WRAPPER_ASSIGNMENTS = (
    "__module__",
    "__name__",
    "__qualname__",
    "__doc__",
    "__annotations__",
)
WRAPPER_UPDATES = ("__dict__",)


def update_wrapper(
    wrapper,
    wrapped,
    assigned=WRAPPER_ASSIGNMENTS,
    updated=WRAPPER_UPDATES,
):
    for attr in assigned:
        try:
            value = getattr(wrapped, attr)
        except AttributeError:
            pass
        else:
            setattr(wrapper, attr, value)
    for attr in updated:
        getattr(wrapper, attr).update(getattr(wrapped, attr, {}))
    # Issue #17482: set __wrapped__ last so we don't inadvertently copy it
    # from the wrapped function when updating __dict__
    wrapper.__wrapped__ = wrapped
    # Return the wrapper
    return wrapper


def wraps(
    wrapped,
    assigned=WRAPPER_ASSIGNMENTS,
    updated=WRAPPER_UPDATES,
):
    return partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated)


def is_admin(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        # NOTE: will fail if username is not passed as kwarg
        # username = kwargs.get("username")
        # print("the user name is", username)

        # NOTE: so we need to use inspect which will return a dict that we can search
        func_args = inspect.getcallargs(f, *args, **kwargs)
        username = func_args.get("username")

        if username != "admin":
            raise Exception("You are not an admin!")
        return f(*args, **kwargs)

    return wrapper


@is_admin
def foobar(username="someone"):
    """Do some stuff."""


# foobar()


@is_admin
def foobar2(username):
    """Do some stuff."""


# NOTE: will fail in the first case, and then work in the second once we use inspect
foobar2("admin")
