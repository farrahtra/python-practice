### TOPIC: if-else statements
### DESCRIPTION: An 'if-else statement' evaluates an expression, if the expression is true, it executes some code, if the expression is false, it executes other code.

## SUBTOPIC: Booleans

# a boolean is a data type that can be True or False.

# a boolean cannot be any other thing, besides True or False.

# Here we create a boolean called 'isNight' and set it to False

isNight = False

# Here we create a boolean called 'isDay' and set it to True

isDay = True

# we can use booleans to make decisions in a program

## SUBTOPIC: Booleans in if-else statements

# this is an if-else statement

if isDay:
    print("it's daytime")
else:
    print("it's not daytime")

# this if statement prints "it's daytime" if isDay is True and prints "it's not daytime" if isDay is False

## EXERCISE 1

# In the above if-else statement, what is printed?

## EXERCISE 2

# okay, let's try another, what is printed from the below code

if isNight:
    print("it's nighttime")
else:
    print("it's not nighttime")

## EXERCISE 3

# Okay, last one! Let's tell a short story

# aiden wants to keep track of how many apples he eats

aidens_apples = 0

# aiden eats an apple every monday

# today is monday

isMonday = True

if isMonday:
    aidens_apples = aidens_apples + 1

# today is tuesday

isMonday = False

if isMonday:
    aidens_apples = aidens_apples + 1

# how many apples does aiden have?

## SUBTOPIC: if-else statements with expressions

# when  you have an expression like 1 > 0 (one greater than zero) it evaluates automatically, in this case to True because 1 is greater than 0

# so we can use this in an if-else statement

if 1 > 0:
    print("1 is greater than 0")
else:
    print("1 is not greater than 0")

## EXERCISE 4

# what is printed above?

## SUBTOPIC: entering the pool

# storytime again

# mike is 10

mike = 10

# he wants to go to the pool

# but he has to be 15 to go to the pool

age_to_enter = 15

if mike > age_to_enter:
    print("you can enter the pool")
else:
    print("you cannot enter the pool")

# so he can't enter the pool

# ted is 17

ted = 17

# he wants to go to the pool

if ted > age_to_enter:
    print("you can enter the pool")
else:
    print("you cannot enter the pool")

# and he is able to enter

## EXERCISE 5

# what will the following code print?

age_to_enter = 20
age_to_enter_sea = 25
age_to_enter_jacuzzi = 15

kelly = 19

if kelly > age_to_enter:
    print("you can enter the pool")
else:
    print("you cannot enter the pool")

if kelly > age_to_enter_sea:
    print("you can enter the sea")
else:
    print("you cannot enter the sea")
    
if kelly > age_to_enter_jacuzzi:
    print("you can enter the jacuzzi")
else:
    print("you cannot enter the jacuzzi")
    
