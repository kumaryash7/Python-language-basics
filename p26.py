import string


s1=str(input())
s2=str(input())
count=0
for i in range(0,len(s1)):
    if s1[i]!=s2[i]:
        count=count+1


if count%2==0:
    print("Yes")

else:
    print("No")
