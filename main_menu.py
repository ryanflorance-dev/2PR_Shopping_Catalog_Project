def mainmenu():
    start = 0
    print(f"Welcome")
    print("1: start game")
    print("2: quit")
    option = input()
    if option == 1:
        start = 1
        return start
    elif option == 2:
        pass
    else:
        print("Error, must pick an actualy option. Reason for this error may be one of the following:")
        print("Number you selected is more than 2,")
        print("Number you selected is less than 1,")
        print("Number you selected is a decimal,")
        print("You wrote out the number instead of using the digit.")

