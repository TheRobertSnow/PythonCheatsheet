#  try exception is used to try and do stuff but doesn't stop the program from running if it ends up in a error.
aString = "123"
aInteger = 123

# basic explanation
try:
    newVariable = aInteger + aString  # tries to add a string to a integer that results in a error
except:  # you can use "except" for all errors, but specifying what error you'r handling is better practice.
    aString = int(aString)
    newVariable = aInteger + aString

# test what error you get and you can use that error to specify how the program should handle what error you have..

try:
    newVariable = aInteger + aString  # tries to add a string to a integer that results in a error
except TypeError:  # if we get the error "TypeError" we use this exception.
    aString = int(aString)
    newVariable = aInteger + aString
except FileNotFoundError:  # if we were f.x. doing many things that can result in a many errors...
    # we can have many exceptions to handle what error you have.
    pass

# loop until we don't get a error
filename = input("what file do you want to open")
while True:
    try:
        file_object = open(filename, "r")
        break  # only reaches our break if we didn't get a error
    except FileNotFoundError:
        filename = input("oops, we don't have that file. Try again")





