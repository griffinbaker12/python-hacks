class Test:
    def m(self): ...


t = Test()
method_obj = t.m
print(id(method_obj))

new_method_obj = t.m
print(id(new_method_obj))

# these method objects give python a way to remember the function
# and the instance it should operate on

print(method_obj.__self__)
print(method_obj.__func__)
print(method_obj.__class__)

# This is why creating new bound methods is cheap - it's just creating a tiny C struct with a few pointers, and the actual function code is shared!
