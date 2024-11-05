from typing import Dict, Union


class Test:
    def __init__(self) -> None:
        self.age = 1000


t = Test()

try:
    print("the age is", t.age)
except AttributeError:
    print("att error")
else:
    print("no att error")


d: Dict[str, Union[str, int]] = {"name": "joe"}
d.update({"age": 16})

print(d)
