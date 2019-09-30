# cheat sheet um strengjavinnslu, output er það sem kæmi ef þu myndir gera print(myString)

# ATH strengurinn er alltaf að breytast þannig ef þið prufið að gera print í þessu skjali mun það ekki koma rétt út
myString = "This is a string"


# Delete the last character
myString = myString[:-1]  # output - "This is a strin"


# Only get the last character
myString = myString[-1]  # output -  "g"


# cut the first 3 characters and the last 2 characters.
myString = myString[3:-2]  # output - "s is a stri"


# steps 2 each time
myString = myString[::2]  # output - "Ti sasrn"


# step backward
myString = myString[::-1]  # output - "gnirts a si sihT"


# replace in a string(example replaces first character)
myString = "A" + myString[1:]  # output - "Ahis is a string"

# make everything upper in a string
myString = myString.upper()  # output - "THIS IS A STRING"
# same can be done with .lower for lowercase, useful to check f.x. if input is "a" since "A" and "a" aren't the same

# find X in string
myString.find("s")  # output - 3 (our first "s" is in index number 3
myString.find("STRING")  # output - -1 we don't have uppercase "string" in our string so it returns -1 (failed)
myString = "This is a string"
myString.upper().find("STRING")  # output - 10 beginning of "string" is at index 10
myString.find("s", 7)  # find "s" in our string, but start at index 7, outputs 10

# format method
myString = "{} is a string".format("this")  # outputs "this is a string", can also use variables in parenthesis


# length of string
len(myString)  # outputs 16


# splitting a string
one, two, three, four = myString.split(" ")  # splits our string on each space and puts each split into the variables
# one = "this" | two = "is" | three = "a" | four = "string"
# can split on whatever you want f.x. "," or "@"...

# alignment format
for n in range(3,11):
    print('{:4}-sides:{:6}{:10.2f}{:10.2f}'.format(n, n*10, n*100, n*1000))  # "{:4} pushes it 4 spaces to the right
    # and starts there, then {:6} pushes it 6 spaces to the right and starts there and so on...
    """outputs = 
    3-sides:    30    300.00   3000.00
    4-sides:    40    400.00   4000.00
    5-sides:    50    500.00   5000.00
    6-sides:    60    600.00   6000.00
    7-sides:    70    700.00   7000.00
    8-sides:    80    800.00   8000.00
    9-sides:    90    900.00   9000.00
   10-sides:   100   1000.00  10000.00
    """
