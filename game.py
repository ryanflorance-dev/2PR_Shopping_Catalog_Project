def mainmenu():
    print(f"Welcome")
    print("1: start game")
    print("2: quit")
    global start
    start = 0
    option = int(input())
    if option == 1:
        start += 1
        return start
    elif option == 2:
        start += -1
        return start
    else:
        print("Error, must pick an actualy option. Reason for this error may be one of the following:")
        print("Number you selected is more than 2,")
        print("Number you selected is less than 1,")
        print("Number you selected is a decimal,")
        print("You wrote out the number instead of using the digit.")

def game():
    pass

mainmenu()
if start == 1:
    game()
elif start == -1:
    pass
else:
    print("Error")