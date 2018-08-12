pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda p:p[1])
print(pairs)

def a():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    :return:
    """
    pass
print(a.__doc__)

