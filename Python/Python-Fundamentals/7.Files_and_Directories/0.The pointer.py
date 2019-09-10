"""
An important concept when dealing with files is the cursor.
You can think of it as the pointer that is moved when we do read/write operations.
For example, the readline method returns the next line in the file and moves the cursor to the line below.
Therefore, when we call the method again it would return the next line.
Once the open function is called, the cursor is placed at the beginning of the file except we are using the append mode,
then the cursor is placed at the end of the file.
"""

with open('test2.txt', 'r+') as file:           # the pointer is аt the start of the file by default
    print(file.read())                          # the pointer will be moved to the end of the file
    file.write('\nAppend one line from [(The pointer)Read and write at the same time.py]\n')

# Every open file has an implicit pointer which indicates where data will be read and written.
# Normally this defaults to the start of the file, but if you use a mode of a (append) then it defaults to the end of the file.
# It's also worth noting that the w mode will truncate your file (i.e. delete all the contents) even if you add + to the mode.
# Whenever you read or write N characters, the read/write pointer will move forward that amount within the file.
# https://stackoverflow.com/questions/14271216/beginner-python-reading-and-writing-to-the-same-file

'''
Most commonly, when we read information from files we read it through a loop. 
Within the loop we extract the information based on the organisation of the text file. 
It is common to read line by line and save the information into a list 
or directly process it with some defined functions.
'''

'''
Using all mode values but 'r' allow us to write content to the opened file.
If any content is present in the opened file along with 'w' mode value
any previous information in the file will be lost.
'a' will append any new content to the end of the file. 
If + is added to the end, the file gets open in both modes (read+write, etc.)
https://stackoverflow.com/questions/1466000/python-open-built-in-function-difference-between-modes-a-a-w-w-and-r
If you want to open an existing file for read and write, 
you should better use "r+", because this will not delete the content of the file.
'''

# Basically w and a create a new file if it doesn't exist
