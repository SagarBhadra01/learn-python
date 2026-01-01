#file handling write

# Open a file in write mode
with open('file_02.txt', 'w') as file:
    # Write some text to the file
    file.write('Hello, World!\n')
    file.write('This is a test file.\n')
    file.write('File handling in Python is easy!\n')    
# The file is automatically closed when the with block is exited
print("Data written to file_02.txt")
# Open the file in read mode to verify the content
with open('file_02.txt', 'r') as file:
    content = file.read()
    print("File Content:")
    print(content)
# The file is automatically closed when the with block is exited