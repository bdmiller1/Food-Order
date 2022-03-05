#Assignment #4 by Bahna Miller
def welcome():
    print("Welcome to Scary Fast Food! We fry everything!")
    print("*                                            *")

def gimmeFood(someArray):
    answer = input("What would you like to add to your order?\n")
    someArray.append(answer)

def showFood(someArray):
    print("Your food order contains the following delicacies:")
    for items in someArray:
        print(" * " + items)

def removeFood(someArray):
    answer2 = input("What would you like to remove from order?\n")
    someArray.remove(answer2)
#my food goes in the array(list), foodOrder
foodOrder = []
#put your list here. This is now appending to the list

welcome()
done = ""
while not done:
    do = input("Please (A)dd to your order, (D)isplay your order, (R)emove form your order, or e(X)it:\n")
    action = do[0]
    if action == "a" or action == "A":
        gimmeFood(foodOrder)
    elif action == "d" or action == "D":
        showFood(foodOrder)
    elif action in ["r", "R"]:
        removeFood(foodOrder)
    elif action in ["x", "X"]:
        print("goodbye")
        done = True
    else:
        print("Yo, um, maybe you suck at typing bruhv")
