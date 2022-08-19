# File Input and Output In Python
# open function for opening files
# open function has two paramters --> filename and mode


f = open('sample.txt', 'r')

# By default the mode is r--> reading a file

data = f.read()

print(data)

data2=f.readline()
print(data2)


f.close()
