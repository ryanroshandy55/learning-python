import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

print("-----------")

# Metacharacters
# Metacharacters are characters with a special meaning:

# Character	Description	Example	Try it
# []	A set of characters                         	"[a-m]"	
# \	    Signals a special sequence  
    # (can also be used to escape special characters)	"\d"	
# .	    Any character (except newline character)        "he..o"	
# ^	    Starts with                                 	"^hello"	
# $	    Ends with                                   	"planet$"	
# *	    Zero or more occurrences                    	"he.*o"	
# +	    One or more occurrences                     	"he.+o"	
# ?	    Zero or one occurrences                     	"he.?o"	
# {}	Exactly the specified number of occurrences 	"he.{2}o"	
# |	    Either or                                   	"falls|stays"	
# ()	Capture and group

# Special Sequences
# A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

# Character	Description	Example	Try it
# \A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
# \b	Returns a match where the specified characters are at the beginning or at the end of a word     r"\bain"
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	        # r"ain\b"	

# \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word  r"\Bain"
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	                        r"ain\B"	


# \d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
# \D	Returns a match where the string DOES NOT contain digits            "\D"	
# \s	Returns a match where the string contains a white space character	"\s"	
# \S	Returns a match where the string DOES NOT contain a white space character	"\S"	
# \w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
# \W	Returns a match where the string DOES NOT contain any word characters	"\W"	
# \Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"	


# Sets
# A set is a set of characters inside a pair of square brackets [] with a special meaning:

# Set	    Description	Try it
# [arn]	        Returns a match where one of the specified characters (a, r, or n) is present	
# [a-n]	        Returns a match for any lower case character, alphabetically between a and n	
# [^arn]	    Returns a match for any character EXCEPT a, r, and n	
# [0123]	    Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
# [0-9]	        Returns a match for any digit between 0 and 9	
# [0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
# [a-zA-Z]	    Returns a match for any character alphabetically between a and z, lower case OR upper case	
# [+]	        In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string


# The findall() function
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

# Return an empty list if no match was found:
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

# The search() function

# Search for the first white-space character in the string:
txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

# Make a search that return no match
txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

# The split function
# Split at each white-space character:
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

# The sub() funciton
# The sub() function replaces the matches with the text of your choice:
# Replace every white-space character with the number 9:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

# replace the first 2 occurrences:
txt = "The rain in Spain"
x = re.sub("\s", "-", txt, 2)
print(x)

print("-----------")


# Match Object
# Do a search that will return a Match Object:
import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object

print("-----------")


# Print the position (start- and end-position) of the first match occurrence.
# The regular expression looks for any words that starts with an upper case "S":
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

print("-----------")


# Print the string passed into the function:
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

print("-----------")

# Print the part of the string where there was a match.
# The regular expression looks for any words that starts with an upper case "S":
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())