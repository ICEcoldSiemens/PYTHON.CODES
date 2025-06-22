# As a dynamically typed programming language, there is no need to manually assign the data type
# Additionally, no need to end statements with a semicolon.

# Variables -> containers which stores values. We can perform multiple assignments on a line
age, money, first_name, last_name, isReal = 20, 0.00, "Somto", "Ezeoke", False

# We can commit multiple assignments of variables of the same value on the same line
cookies = pizza = donuts = 10

# We can manipulate strings to multiple with integers
print(cookies*3)

# Prints the data type of the variable -> in this case, it is a string
print(type(first_name))

# Applying string concatenation to print value of 'name' and desired output
print ("Hello, my name is " + first_name + " " + last_name + ". I am learning Python programming.")

# The integer value must be converted into a string literal for string concatenation to work.
print("I will be " + str(age + 1) + " next year.")

# The float value of 'money' is printed
print("I have £" + str(money) + "p in my bank account.")

# The boolean value of 'isReal' is printed
print("I am real: " + str(isReal))