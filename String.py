# Strings in python are surrounded by either single or double quotation marks.
# Example : 'Abhi' is same as "Abhi"

# In python programming if you want to display the string literal, then you can use the print() function

# You can use quotes inside a string, as long as they don't match the quotes surrounding the string:

print("It's alright")

# Assign string to a variable:
# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

a = "Hey What's up"
print(a)

# Multiline Strings

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# String are arrays
# Like many other popular programming languages, strings in Python are arrays of unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.

a = "Hello, World!"
print(a[1])

#Looping through a String
for x in "Abhisekh":
    print(x)

# String Length
a = "Hello World..."
print(len(a))    


# Check String
# To check if a certain phase or character is present in a string, We can use the keyword "in".
a = "Lorem ipsum dolor sit amet"
print("Lorem" in a)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


# Check if NOT
# To check if a certain phase or character is not present in a string, We can use the keyword "not in"

txt = "The best things in life are free!"
print("expensive" not in txt)



