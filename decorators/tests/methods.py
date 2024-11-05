class Test:
    def __init__(self, size):
        self.size = size

    def get_size(self):
        return self.size


t = Test(5)
print(t.get_size())  # 5

print(t.get_size is Test(10).get_size)
print(t.get_size, Test(10).get_size)


class Test2:
    def __init__(self, size):
        self.size = size


print(Test.get_size(Test2(10)))  # type: ignore

print(t.get_size.__func__ is Test(10).get_size.__func__)

print(Test.__dict__["get_size"])

print(t.get_size.__class__)
print(t.__dict__)

print(t.get_size is t.get_size)
