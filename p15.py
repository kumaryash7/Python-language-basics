a = int(input("Enter num 1 :"))
b = int(input("Enter num 2 :"))
c = int(input("Enter num 3 :"))
# we use and or keywords instead of && and || in python
if(a > b and a > c):
    print(a)
elif(b > a and b > c):
    print(b)
else:
    print(c)


# Use of in keyword in python
e=[1,2,3]
print(1 in e)
