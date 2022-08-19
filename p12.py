# dictioniary methods
myDict = {

    "Yash": "In a Quick Manner",
    "Punnet": "Wow ",
    "Marks": [1, 2, 4],
    "Age": 10,
    "anotherDict": {"Name": "Yash"},  # nested dictioniary
    1: 100  # key value pair can be integers too
}

print(list(myDict.keys()))  # Prints the keys of the dictioniary as a list
print(myDict.values())

# prints the all key value pairs of the contents of the dict.
print(myDict.items())

print()
print()
print()
print()

print(myDict)
updateDict = {

    "Lovish": " A New Friend",
    "Puneet": "Another new friend"
}


myDict.update(updateDict)

print(myDict)

print(myDict.get("Punnet"))
