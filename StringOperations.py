# Slicing Strings
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index,
# separated by a colon, to return a part of the string.

x = "Hello, World !"
print(x[4:10])
# Get the characters from position 4 to position 10(not included)

b = "Hello, World!"
print(b[:5])
# Get the characters from the start to position 5 (not included):

c = "Hello, World !"
print(c[2:])
# Get the characters from position 2, and all the way to the end:

# Negative Indexing
b = "Hello, Buddy"
print(b[-5:-2])


# Modify Strings

# Upper Case:
# The upper() method returns the string in upper case:
a = "Hello,Buddy"
print(a.upper())

# Lower Case:
# The lower() method returns the string in lower case:
a = "Hello,Buddy"
print(a.lower())

# Replace:
# The replace() method replaces a string with another string:

a = "Hello buddy,How are you?"
print(a.replace("buddy","World")) 

# Split:
# The split() method splits the string into substrings if it finds instances of the operator

a = "Hello, World"
print(a.split(","))


# String Concatenation :
# To concatenate, or combine, two strings you can use the + operator

a = "Hey"
b = "Buddy"
c = a + b
d = a+" "+b
print(c)
print(d)