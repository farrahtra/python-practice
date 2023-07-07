### TOPIC: Booleans

# previously we discussed the number datatype, now we will introduce another datatype called a Boolean

# While a number has many possible values, a Boolean has only two, True or False

# let's set a variable (isBlue) to True

isBlue = True

# now we can print this variable to the console

print(isBlue)

# now let's set the variable isRed to False

isRed = False

# but why do we have booleans?

# one use case is a logical expression, we can combine booleans with keywords 'and' or 'or' which reads each value and returns a new value, let's see

# using the 'and' keyword, it will evaluate if both variables are True, and if so, return True, otherwise False

isACircle = True
isGreen = True

# now we create another variable combining isACircela and isGreen

isAGreenCircle = isACircle and isGreen

print(isAGreenCircle) # True

# This will print out true because both isACircle and IsGreen are True

# suppose we want to check if we have a red circle

isARedCircle = isACircle and isRed

print(isARedCircle) # False

# but why was this false? because isRed is False
