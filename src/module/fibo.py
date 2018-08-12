def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

def fib2(n):
    r = []
    a, b = 0, 1
    while a < n:
        r.append(a)
        a, b = b, a + b
    return r

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
