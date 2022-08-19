
from audioop import reverse


l = [3, 5, 1, 3, 2, 2, 8]

l.sort()

print(l)
l.reverse()

print(l)

l.append(10000)  # appends/adds at the end of the list
print(l)


l.insert(3, 800)
print(l)


l.pop(1)
print(l)

l.remove(2)
print(l)
