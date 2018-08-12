def reverse(data):
    for index in range(len(data)-1, -1, -1):
        # 每次调用next()时，将会在停止的地方恢复，并激继续返回
        yield data[index]

for c in reverse('golf'):
    print(c, end=" ")
print()
