### TOPIC: Booleans II - and

# last lession we introduced booleans, and the `and` keyword

# we saw that True and True is True, but what about if we put other
# boolean values?

# Take a minute to guess the output of these print statements

print(True and False)
print(False and False)
print(True and False)

# as stated before when you `and` two values, the result will be true
# if and only if both values are True

# Hence all three statements are false because in each other not both
# are True

# don't worry about these lines
from boolean_data import isBlue
from boolean_data import isRed
from boolean_data import isCircle
from boolean_data import isSquare

# okay we've imported some mystery variables

# now based on these print statements, what shape and color do we
# have?

print(isBlue and isCircle)
print(isRed and isSquare)
print(isRed and isCircle)
