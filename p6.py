# a = '''  "yash"  '''
# print(a)




name = "YashIsAGoodBoy"

print(name[2])
# first one is including and last one is excluding i.e, 0-(n-1)
print(name[0:3])


# negative index prints from last end of string
print(name[-1])


# slicing with a skip value

d = name[1::2]
print(d)

story = "once upon a time there was a boy named Yash Kumar"

# String Functions

print(len(story))

print(story.endswith("Kumar"))
print(story.count("a"))
# capitalises first letter of string
print(story.capitalize())

print(story.find("Yash"))
# Replaces all new words from old words of the string
print(story.replace("Yash", "Puneet"))
