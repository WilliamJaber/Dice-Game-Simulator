# PHASE TWO: Start coding the steps! YOu may have to change step, that is ok!
# The important thing is you have a BLUE-Print or a Plan! So let's start coding!
#-------------------------------------------------------------

# STEP 1: Import random module
from random import randint

#-------------------------------------------------------------
# STEP 2: Create a Data Structure to store dice-roll results
d = {k:0 for k in range(3, 12)}  # Dictionary comprehension.
# The Syntax is: {key:value for (key, vaue) in interable}.
# The logic of my dictionary comprehension is => create a "key" variable (k), and set the
# default "value" to zero for every key in range 3, 12. I chose range 3-11
# because I plan to count my doubles deferently. I don't coun't 12 because 12
# will be a double no matter what: (*only 6 and 6 can produce 12).
# Of course I am not done. I must modify my dictionary even more to include 'doubles
# and Snake eyes. So lets update our dictionary:
d.setdefault('snakeEyes', 0)
d.setdefault('doubles', 0)

## Our dictionary now looks like this:
## {3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 'snakeEyes': 0, 'doubles': 0}
#-------------------------------------------------------------

# Step 3: Ask user how many roll simulation that want to run:
dice_roll = int(input('How my dice roll simulations?\n> '))
#-------------------------------------------------------------
# # STEP 4: Create a loop for desired iteration
for i in range(dice_roll):
    #-------------------------------------------------------------
    # STEP 5: Create two (2) die objects
    ## Remeber this used to be step (2): But as I said you may have to change
    ## steps as you go through the coding process?!
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    #-------------------------------------------------------------
    # STEP 6: Store the sum of dice1 and dice2 in a data structure
    # Let's establish snakeEyes First - because it should have presidence
    # over doubles:
    # If dice1 and dice2 equal 2( i.e. snake eyes) add it to the dictoinary
    if d1 + d2 == 2:
        d['snakeEyes'] += 1
    # elif dice1 and dice2 equal doubles ( i.e. (3, 3) (4, 4) etc add it to the dictoinary
    elif d1 == d2:            
        d['doubles'] += 1
    # Else - everything else (i.e. 3, 4, 5, 6, 7 etc) : add to dictionary 
    else:
        d[d1+d2] += 1
#-------------------------------------------------------------
# STEP 7: Print Results
print(f'--- Results of {dice_roll} rolls--- ')
# This is how you iterate through a dictionatry (key, value) pair. This
# is like a for loop using 2 variables. It translates to: for key, value
# in dictionary.items()  .items() is enumerating keyes, and values.

# Again, for key, value in dictionary items() - because I want both keys
# and values from dictionary.
for k, v in d.items():
    # I am printing key, value and getting percentage of dice_roll 
     print(f"You rolled {k}, {v} times at {100 * (v/dice_roll):.2f}%")




