from modules.functions import getMenu, checkStock, shop, checkBasket, modify, checkOut, account, getName

# The main function handles the introduction & main menu
def main(name):
    if not name:
        return      
    print(f"\nWelcome back, {name}")  
    print("")

    while True:
        user_choice = getMenu()
        if user_choice == 1:
           checkStock()
        elif user_choice == 2:
            shop()
        elif user_choice == 3:
            checkBasket()
        elif user_choice == 4:
            modify()
        elif user_choice == 5:
           checkOut()
        elif user_choice == 6:
           account()
        elif user_choice == 7:
            exit()
            break
     
# --------------------Main routine--------------------    
if __name__ == "__main__":
    #This is to get the name first and then pass it into main
    while True:
        user_name = getName()
        if user_name:
            main(user_name)