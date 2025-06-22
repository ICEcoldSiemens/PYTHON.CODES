# We can use methods to manipulate string literals
statement = "i like pizza"

#String method list:
# Returns and prints the string length.
print(len(statement))

# Returns and prints the first index of the desired character/string.
print(statement.find("like"))

# Returns and prints the first character in upper capitals.
print(statement.capitalize())

# Returns and prints all character in upper capitals.
print(statement.upper())

# Returns and prints all character in lower capitals.
print(statement.lower())

# Returns and prints the boolean value if string literal is a digit.
print(statement.isdigit())

# Returns and prints the boolean value if string literal has alphabetical characters.
print(statement.isalpha())

# Returns and prints how many characters are in the string.
print(statement.count("z"))

# Replaces old character with new character in string literal.
print(statement.replace("z", "s"))