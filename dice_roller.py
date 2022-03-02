import random
def main():
    dice_rolls = int(input("How many dice would you like to roll?\n"))
    dice_size = int(input("How many sides does the dice have?\n"))
    dice_sum = 0
    for _ in range(dice_rolls):
        roll = random.randint(1,dice_size)
        if roll == 1:
            print(f'You rolled a {roll}! Critical Fail')
        elif roll == 6:
            print(f"You rolled a {roll}! Critical Success")
        else:
            print(f'You rolled a {roll}')
        
        dice_sum += roll

    print(f'You rolled a total of {dice_sum}')

if __name__== "__main__":
    main()
