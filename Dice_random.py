# Import 'random' module in order to randomize the dice outcome
import random

# Create class call 'diceGen'
class diceGen:

    # Determined the value of the dice that can be randomize
    dice_out = [1, 2, 3, 4, 5, 6]
    dice_result = []

    # Create function 'dice_gen' to randomize the dice
    def dice_gen(self):
        
        # Input the number of dices you want to randomize
        diceNum = int(input("Please enter the number of dice : "))
        
        # Randomize the values of each dice until reaching the number of dices that the user put above
        ## and store it in a list 'dice_result'
        for num in range(diceNum):
            diceGen.dice_result.append(random.choice(diceGen.dice_out))
        print("The result of each dice --> ", diceGen.dice_result)


dice_random = diceGen()
dice_random.dice_gen()
