class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return "Hello World"

    def __init__(self, r, i):
        self.r = r
        self.i = i

x = MyClass(10, 20)
print(x.f())
print(x.r)
print(x.i)

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
