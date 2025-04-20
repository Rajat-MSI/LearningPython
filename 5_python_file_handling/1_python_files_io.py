# python files io

# * file handling operation can be done in the following order
# 1.open a file
# 2.read or write - performing operations
# 3.close the file

# * syntax
# file_object = open(file_name,access_mode,buffering)

# * access_modes in file handling
# r     --->   read opens file in read only
# rb    --->   open file in read only binary format
# r+    --->   it opens file to read and write both
# rb+   --->   it opens file to read and write both in binary format
# w     --->   it opens file in write mode only it creates file if no file
#              exist, and it overwrites the file if previously exist
# wb    --->   it opens file to write in binary format only
# w+    --->   it opens file to write and read both it is different from r+
#              it overwrites the previous file if one exists whereas r+ does not
#              overwrite the previously written file
# wb+   --->   it opens the file to write read both in binary format
# a     --->   it opens the file in the append mode it creates file if not exist
# ab    --->   it opens the file in the append mode in binary format it creates
#              file if not exist
# a+    --->   it opens a file to append and read both it creates file if not
#              exist
# ab+   --->   it opens a file to append and read both in binary format


# * opening file in read mode
print("* opening file in read mode")
p_file = open("file.txt","r")

if p_file:
    print("file opened successfully")

# --------------------------------------------------------------------------

# * writing on a file
print("\n* writing on a file")

# opened in write mode
w_file = open("file.txt","w")
# opened in read mode
r_file = open("file.txt","r")
# written on file
w_file.write("written this using python file handling")
# w_file need to be close to clear buffer than only r_file can read the file
w_file.close()
# reading file data
text = r_file.read()
print("file.txt:",text)


# --------------------------------------------------------------------------

# * with statement

# it is useful in the case of manipulating the files. It is used
# in the scenario where a pair of statements is to be executed with a block
# of code in between
print("\n* with statement")
try:
    a_file = open("file.txt","a+")
    with a_file as file:
        file.write("\nappended this text")
        file.write("\nappended another text")
    print("text appended")
except:
    print("cannot open file")


# --------------------------------------------------------------------------

# * appending on a file
# if we open file in write mode and again write it will overwrite the text
print("\n* appending on a file")

try:
    a_file = open("file.txt","a+")
    text = """\nif we open file in write mode and again 
    write it will overwrite the text"""
    with a_file as file:
        file.write(text)
    print("text appended")
    a_file.close()
except:
    print("cannot open file")

# trying to read data
try:
    r_file = open("file.txt","r")
    with r_file as file:
        text = file.read()
        print("* text on file:")
        print(text)
    r_file.close()
except:
    print("cannot open file")

# --------------------------------------------------------------------------

# * reading file through loop
print("\n* reading file through loop")
r_file = open("file.txt","r")
line = 1
for i in r_file:
    print(f"line {line}:",i)
    line += 1
r_file.close()

# --------------------------------------------------------------------------

# * file pointer position

# python provides the tell() method which is used to print the byte number
# at which the file pointer currently exists. The tell() method returns
# the position of read or write pointer from the file
print("\n* file pointer position")
r_file = open("file.txt","r")
print("file pointer position:",r_file.tell())
# reading file will change pointer position
text = r_file.readline()
print("first line:",text)
print("file pointer position:",r_file.tell())

# modifying file pointer position using seek()
r_file.seek(70)
print("file pointer position:",r_file.tell())
print("reading line from above given position:")
text = r_file.read()
print(text)




