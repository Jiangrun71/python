from typing import Iterable, Iterator
name = "张江"
m = iter(name)
print(next(m))

print(isinstance(m, Iterator))