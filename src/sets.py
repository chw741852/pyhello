basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)
print('crabgrass' in basket)

a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

c = {x for x in 'abracadabra' if x not in 'abc'}
print(c)

d = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
print(d)
print(reversed(d))
print(sorted(set(d)))
