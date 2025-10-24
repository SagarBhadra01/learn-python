f = open("file_01.txt", "r")
data = f.read()
print(data)
f.close()

# Alternative way using 'with' statement
with open("file_01.txt", "r") as f:
    data = f.read()
    print(data)
# The 'with' statement automatically handles closing the file

#read only parts of the file
with open("file_01.txt", "r") as f:
    part = f.read(5)  # Read first 5 characters
    print(part)
    rest = f.read()   # Read the rest of the file
    print(rest)

#read line by line
with open("file_01.txt", "r") as f:
    line1 = f.readline()
    print(line1)
    line2 = f.readline()
    print(line2)

#read all lines into a list
with open("file_01.txt", "r") as f:
    lines = f.readlines()
    print(lines)

#iterate through the file line by line
with open("file_01.txt", "r") as f:
    for line in f:
        print(line)

#check if file is readable
with open("file_01.txt", "r") as f:
    if f.readable():
        print("The file is readable.")
    else:
        print("The file is not readable.")
# Note: In read mode, the file is always readable.

