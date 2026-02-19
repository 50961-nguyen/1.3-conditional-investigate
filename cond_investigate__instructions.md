## Setup
1. Git Clone this repository and save it in your inestigate folder.
2. Open this folder on your computer and create a new file called cond_investigate.py

## Instructions

### Play
Take the following program and play around with the value of the variables.

### Submission

All you need to do is create one more variable of your choice (must not be a boolean type) and create an if - else block for that variable... you may print whatever you wish for both the True and False case

## Code
```python
"""
author:
date:
A conditional investigation
"""

# Input - intialize variables
is_cold_outside = True
favourite_number = 42
name_of_hero = "Richard Feynman"
e = 2.71828
#TODO: add one more variable to use in the output section

# Processing - the if-elif-else statements below will process the variables and create outputs base on the conditions

# Output

if is_cold_outside:
    print("Geez man, I'm freezing")
else:
    print("I'm glad I didn't bring a jacket")


if favourite_number < 10:
    print("You have pretty low standards 👀")
elif favourite_number < 20:
    print("You've got an alright personality ⭐")
elif favourite_number < 30:
    print("There are some good people in this world 🤗")
elif favourite_number < 40:
    print("Faith in humanity restored 🎉")
else:
    print("You must control life, the universe, and everything 🤯")


if "e" in name_of_hero:
    print("You probably have a pretty mid hero")
elif "x" in name_of_hero:
    print("Your hero is pretty cool")

if name_of_hero.lower() == "the flash":
    print("Dawg, your zoomin!")
elif name_of_hero.lower() == "superman":
    print("🙄")
else:
    print("Is it even a superhero??")

if e > 3:
    print("Incorrect")
elif e < 2:
    print("Also incorrect")
else:
    print("You probably got it!")

# Check to see if a number is a float
if int(e) == e:
    print("e must be a whole number")
else:
    print("e must have decimals")

#TODO: create an if-else block using your variable. 

```