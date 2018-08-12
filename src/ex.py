# try:
#     raise NameError('HiThere')
# except:
#     print('An exception flew by!')
#     raise

try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world')
