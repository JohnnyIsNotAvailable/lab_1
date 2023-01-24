a = "Hello, World!"
print(a.upper())
#output HELLO, WORLD!

print(a.lower())
#output hello, world!

a = " Hello, World! "
# The strip() method removes any whitespace from the beginning or the end
print(a.strip()) 

# returns "Hello, World!"

#The replace() method replaces a string with another string
a = "Hello, World!"
print(a.replace("H", "J"))

#The split() method splits the string into substrings if it finds instances of the separator:
print(a.split(",")) 
# returns ['Hello', ' World!']

