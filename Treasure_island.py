print("Welcome to Treasure island \nYour mission is to find the treasure\nYou're at a cross road.where do you wnat to go?\n")
select=input('Type "left" or "right". ').lower()
if select=="left":
    left=input("There is a lake with crocodiles here.do you want for a boat  or you want to swim across: ").lower()
    if left=="swim":
        print("OOPs you lost!! coz you are bitten by crocodile ")
    if left=="wait":
        color=input("Great!!You safely came to the island.\nThere are three doors of colors red,blue and yellow.Which door would you like to choose:red,yellow or blue.").lower()
        if color=="red":
            print("Oops there is a fire. Game over!!")
        if color=="blue":
            print("Oops there is a lion.Game over!!!")
        if color=="yellow":
            print("You done it!!!You win the game.")
else:
    print("OOps!!!You have fall into the hole.Game Over")