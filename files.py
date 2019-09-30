"""
    permission types :
   |----------------------------------------------------------------------------------------------------|
   | MODE | How opened      | File exists                       | File Does not exist                   |
   |________________________|___________________________________|_______________________________        |
   | 'r'  | read only       |   Opens that file                 |   Error                               |
   |________________________|___________________________________|_______________________________________|
   | 'w'  | write only      |   Clears the file contents        |   Creates and opens a new file        |
   |________________________|___________________________________|_______________________________________|
   | 'a'  | read and write  |   File contents left intact       |   Creates and opens a new file        |
   |                        |   and new data appended at        |                                       |
   |                        |   file's end                      |                                       |
   |________________________|___________________________________|_______________________________________|
   | 'r+' | read and write  |   Reads and overwrites from the   |   Error                               |
   |                        |   the file's beginning            |                                       |
   |________________________|___________________________________|_______________________________________|
   |  'w+'| read and write  |   Clears the file contents        |   Creates and opens a new file        |
   |________________________|___________________________________|_______________________________________|
   |  'a+'| read and write  |   File contents left intact and   |   Creates and opens a new file        |
   |                        |   read and write at file's end    |                                       |
   |----------------------------------------------------------------------------------------------------|
"""
# often functions are used to f.x. open or write files but this is just basic code that you can adapt.


# open file named "test.txt" for reading ('r')
data_file = open("test.txt", 'r')
# iterate through the file one line at a time
for line in data_file:
    print(line)
data_file.close()  # closes the file.

# Write in a txt file
myVariable = "programming can be fun"
temp_file = open("temp.txt", "w")  # creates the file if it doesn't exist, see table at top
print("This is the first line", file=temp_file)
print("This is the second line", file=temp_file)
print(myVariable, file=temp_file)
temp_file.close()
"""outputs :
This is the first line
This is the second line
programming can be fun
"""

# copy one txt file to another
with open("temp.txt") as f:
    with open("out.txt", "w") as f1:
        for line in f:
            # can use if here f.x. and only write lines with "programming" in it (example)
            f1.write(line)
f.close()
f1.close()
"""outputs :
This is the first line
This is the second line
programming can be fun
"""






