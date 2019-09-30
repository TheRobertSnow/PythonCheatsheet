# cheat sheet on lists

emptyList = []  # creates a empty list
myList = ["arnar", 123, "False", False]  # creates a list with these values
nestedList = [[1, "arnar"], [2, "daði"], [3, "steinþorsson"]]
# !!
# ATH að outputs miða við upprunulega listana þott hann breytist alltaf eftir hverja skipun.
# !!

# adding values to the end of a list
myList.append("last index")  # outputs - ['arnar', 123, 'False', False, 'last index']


# get value from index
myList[1]  # outputs 123
nestedList[2][1]  # outputs "steinþorsson"
myvar = myList[1] # myvar = 123

# get value from index (another way), var eh astæða fyrir að þetta virkaði bara i sumum tilfellum
# man ekki hvaða tilfelli en henti þessu bara með til að hafa.
myList.pop(0)  # outputs - [123, 'False', False, 'last index']
getValue = myList.pop(0)  # getValue is now "arnar" but the list still loses the index
# we can work around this without affecting our list by making a copy.
secondList = myList[:]  # copies our entire list.
getValue = secondList.pop(2)  # now our second list loses the value "False" but our original doesn't


# lists work similar as strings
myList[-1]  # outputs - False       (boolean not string)
myList[::2]  # outputs - ['arnar', 'False']
myList[0:2]  # output - ['arnar', 123] - gets index 0, 1 but stops at 2
123 in myList  # output - True  (boolean)
myList = myList*3  # output -['arnar', 123, 'False', False, 'arnar', 123, 'False', False, 'arnar', 123, 'False', False]
myList.extend("abcs")  # output - ['arnar', 123, 'False', False, 'a', 'b', 'c', 's']
#myList.remove(123)  # output - ['arnar', 'False', False]
myList.reverse()  # output - [False, 'False', 123, 'arnar']
#myList.sort()  # outputs an error! can't sort booleans and strings, works with ints and strings(only int or only str)
myList.insert(1, "something new!")  # outputs - ['arnar', 'something new!', 123, 'False', False]
# munið að .pop() deletar indexinu.


# create a nested list with our empty list
for x in range(10):
    emptyList.append([])  # creates a empty nested list
    for i in range(2):
        emptyList[x].append(i+x)  # puts values in the nested list
# output of for loop - "[[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]"


# loop through a list
for x in myList:  # loops through myList
    pass


# accessing nested list information
nestedList = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], ["abs", "bcs"]]
# lets say we want to find the list with values 5 and 6 in it and change it to 12 and 13
# enumerate explanation : loops is how many times we have loops, element is the element in our list
for loops, element in enumerate(nestedList):  # loops through our list, x is
    if 5 in element and 6 in element:
        nestedList[loops] = [12, 13]
# outputs - [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [12, 13], [6, 7], [7, 8], [8, 9], [9, 10], ['abs', 'bcs']]


