# PHASE THREE: Now it's time to refactor code which is the process of
# restructuring computer code without changing or adding to its external
# behavior and functionality (i.e. let's make it look pretty)..
#-------------------------------------------------------------

from random import randint
import sys

# Let's put everything in a main function:
def main():
    # Dcictionary containing roll frequency:
    d: dict[int, int] = {k:0 for k in range(3, 12)}
    # Update dictionary to inlude snakeEyes and Doubles
    d.setdefault('snakeEyes', 0)
    d.setdefault('doubles', 0)
    # Get user input for number of rolls
    dice_roll = int(input('How my dice roll simulations?\n> '))
    for i in range(dice_roll):
        # Initialze two (2) dice
        d1 = randint(1, 6)
        d2 = randint(1, 6)
        if d1 + d2 == 2:
            d['snakeEyes'] += 1
        elif d1 == d2:
            d['doubles'] += 1
        else:
            d[d1+d2] += 1
    # Now, print results:
    print(f'--- Results of {dice_roll} rolls --- ')
    for k, v in d.items():
         print(f"You rolled {k}, {v} times at {100 * (v/dice_roll):.2f}%")
    # Play again option:
    play_again()

def play_again():
    """Handles play again option"""
    while True:
        option = input('\nWould you like to play again?! (yes or no): ')
        if option not in ['yes', 'no']:
            print('invalid option!')
            continue
        else:
            break
    if option == 'yes':
        return main()
    else:
        print('Thanks for playing - Goodbye!')
        sys.exit()


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
     main()
