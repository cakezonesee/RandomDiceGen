import random


class diceGen:

    dice_out = [1, 2, 3, 4, 5, 6]
    dice_result = []

    def dice_gen(self):
        diceNum = int(input("Please enter the number of dice : "))
        for num in range(diceNum):
            diceGen.dice_result.append(random.choice(diceGen.dice_out))
        print("The result of each dice --> ", diceGen.dice_result)


dice_random = diceGen()
dice_random.dice_gen()
