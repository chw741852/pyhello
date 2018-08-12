class Mapping:
    def __init__(self, items):
        self.items = []
        self.__update(items)

    def update(self, items):
        for item in items:
            self.items.append(item)

    __update = update

items = [1,2,3,4]
x = Mapping(items)
x.update(items)
print(x.items)

class MappingSub(Mapping):
    def __init__(self, keys, values):
        self.items = []
        self.update(keys, values)

    def update(self, keys, values):
        for item in zip(keys, values):
            self.items.append(item)

y = MappingSub(['a', 'b', 'c'], [1, 2, 3])
print(y.items)

for i in (1,2,3):
    print(i)

for j in [1,2,3]:
    print(j)

for k in {'o': 1, 't': 2}:
    print(k)

class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')
for char in rev:
    print(char, end=" ")
print()

