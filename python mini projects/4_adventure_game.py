name = input("Type your name: ")

print("Welcome", name ,"to this adventure!")

answer = input("you are on a dirt road , it has come to an end and you can go left or right . which way would you like to go? ").lower()

if answer == "left":
    answer = input("you come to a river , you can walk arround it or swim across. type a walk to walk arround it or swim to swim accross?  ")
    if answer == "swim":
        print("You swim accross and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for manymiles, ran out of water and you lost the game.")     
    else:
        print("Not a valid option. You lost.")
    
elif answer == "right":
    answer = input("You come to a bridge , it looks wobby, do you want to cross it or head back(cross/back)")
    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them(yes/no)")

        if answer == "yes":
            print("You talk to the stranger and they give you gold. You WIN!")
        elif answer == "no":
            print("you ignore the stranger and they offended and you lose.")
    
    else:
        print("Not a valid option. You lost.")

else:
    print("Not a valid option. You lost.")
    
    
print("Thank you for trying ",name )