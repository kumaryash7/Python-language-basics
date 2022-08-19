# sets in python

from operator import le


a = {1, 3, 4, 5, 3, 1, 3}
print(type(a))
print(a)

b = {}  # This is an empty dictioniary
print(type(b))

print(b)
c = set()
print(type(c))
print(c)


e = set()

e.add(4)
e.add(4)
e.add(4)
e.add(4)
e.add(5)
e.add(6)
e.add(7)

print(e)

print(len(e))
e.pop()  # removes random value from the set
print(e)

e.remove(6)
print(e)

e.intersection({10})
print(e)