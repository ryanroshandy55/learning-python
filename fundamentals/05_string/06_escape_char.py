# Escape Character
# An escape character is a backslash \ followed by the caracter you want to insert
# example of an illegal character is a double quote inside a string
# txt = "We are the so-called "vikings" from the north"     #error
txt = "We are the so-called \"vikings\" from the north"
print(txt)

# * This is the other list of escape char
# \'	    # Single Quote	
# \\	    # Backslash	
# \n	    # New Line	
# \r	    # Carriage Return	
# \t	    # Tab	
# \b	    # Backspace	
# \f	    # Form Feed	
# \ooo	    # Octal value	
# \xhh	    # Hex value

a = "This for testing: \n python"
print(a)