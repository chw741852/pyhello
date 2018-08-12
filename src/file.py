f = open('workfile', 'rb+')
print(f.write(b'0123456789abcdef'))

print(f.seek(5))
print(f.read(1))

print(f.seek(-5, 2))
print(f.read(1))
