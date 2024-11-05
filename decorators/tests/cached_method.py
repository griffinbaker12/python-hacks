import time


class Pizza:
    def __init__(self, size):
        self.size = size

    def get_size(self):
        return self.size


def cache_bound_methods(cls):
    original_getattribute = cls.__getattribute__

    def __getattribute__(self, name):
        attr = original_getattribute(self, name)
        if not callable(attr) or name.startswith("__"):
            return attr

        # Only cache actual methods
        if not hasattr(self, "_method_cache"):
            object.__setattr__(self, "_method_cache", {})

        if name not in self._method_cache:
            self._method_cache[name] = attr.__get__(self, cls)
        return self._method_cache[name]

    cls.__getattribute__ = __getattribute__
    return cls


@cache_bound_methods
class CachedPizza2:
    def __init__(self, size):
        self.size = size

    def get_size(self):
        return self.size


# Test again
def measure_again():
    regular = Pizza(10)
    cached = CachedPizza2(10)

    iterations = 1000000

    start = time.time()
    for _ in range(iterations):
        method = regular.get_size
    regular_time = time.time() - start

    start = time.time()
    for _ in range(iterations):
        method = cached.get_size
    cached_time = time.time() - start

    print(f"Regular time: {regular_time:.3f}")
    print(f"Cached time: {cached_time:.3f}")
    print(f"Regular same?: {regular.get_size is regular.get_size}")
    print(f"Cached same?: {cached.get_size is cached.get_size}")


measure_again()
