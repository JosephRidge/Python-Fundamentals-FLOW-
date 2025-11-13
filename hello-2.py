"""
- Operators & Operands
    - arithmetic operators:  +, -, /, //, **, *
    - comparison operators: ==, !=, <, >, <=,>=
    - boolean operators: and, or, not (Truth table)
    - is operator: identity operator
    - in membership operator 
    - ternary operator  
    - binary operators  ( |, &, ^, <<, >> )

- Data structures
    - Data Types: 
        - boolean
        - number [ int, float, complex]
        - lists
        - tuples
        - dictionaries
        - set


"""

output = "" # general output variable
num1 = 10
num2 = 12

# Operators & Operands

#  arithmetic operators:  +, -, /, //, **, *, %
output = num1 + num2 # addition
output = num1 - num2 # subtraction
output = num1 / num2 # division
output = num1 // num2 # floor division
output = num1 * num2 # multiplication
num1 = 10
num2 = 2
output = num1 ** num2 # power
output = num1 % num2 # modulus

# comparison operators: ==, !=, <, >, <=,>=
firstName = "John"
lastName = "Doe"

num1 = 10
num2 =11
num3 =10

output = firstName == lastName # equality check
output = firstName != lastName # not equality check
output =  num1 > num2 # greater than 
output =  num1 < num2 # less than 
output =  num1 >= num2 # greater than or equal to
output =  num1 <= num2 # less than or equal to

"""
boolean operators: and, or, not (Truth table)
- and: both operands must be true to get a true else false
- or: atleast one must be true
"""
firstName = "John"
secondName = "John"
lastName = "Doe"

num1 = 10
num2 =11
num3 =10

isUserLoggedIn = True
isDarkMode = False

output = (firstName == secondName) and (secondName == lastName)# strict and
output = isUserLoggedIn and isDarkMode # strict and
output = isDarkMode or isUserLoggedIn # flexible OR operator
output = not (isDarkMode or isUserLoggedIn) # not operator-> opposite


# is operator: identity operator  in membership operator
firstName = "Titan"
secondName = "AOT"
lastName = "Titan"

fruits = ["apples", "mangoes", "tomatoes","pineapples"]

output = firstName is secondName
output = firstName is lastName
output = 'i' in lastName
output = "apples" in fruits

if lastName == "AOT":
    output = "AOT !!!"
else:
    output = "Titan"

# ternary operator: <return statement> if <condition> else <return statement>
output = "AOT !!!" if secondName == "AOT" else "Titan"

targetFruit ="green apple"
availableFruit ="green apple"
alternative = "pineapples"

# simple conditinal statement
if targetFruit ==  availableFruit:
    output = "Take green apples!"
else:
    output = "Take pineapples or any cirtic fruit"

#  ternary operator
output = "Take green apples!" if targetFruit ==  availableFruit else "Take pineapples or any cirtic fruit"


output = "hello" if lastname == "okumu" else "its not okumu"


print("================================================")
print(output)
print("================================================")