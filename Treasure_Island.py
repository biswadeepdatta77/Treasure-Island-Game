print("Welcome to Treasure Island!! Your mission is to find the treasure ")
choice = input("Do you want to go left or right? Type 'left' to go left or type 'right' to go right ")
if choice=='right':
    print("Game Over ")
if choice=='left':
    choice2= input("You have reached a lake. Do you want to swim or wait for boat? Type 'swim' to swim or type 'wait' to wait for the boat ")
    if choice2=='swim':
        print("Game Over")
    if choice2=='wait':
        choice3 = input("You have reached in front of thee houses- red, blue and yellow unharmed. Choose which house you want to go? Type 'red' to go to red house or 'yellow' to go to yellow house or 'blue' to go to blue house ")
        if choice3=='blue':
            print("Game Over")
        if choice3=='red':
            print("Game Over")
        if choice3=='yellow':
            print("Congratulations! You Won.")