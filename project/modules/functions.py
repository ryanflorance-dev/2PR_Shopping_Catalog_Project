from data.customer import customers 
import sys, time, re, random, os, subprocess, shutil
from data.stock import stock

# This is to clear the screen on window, linux, mac
def clearScreen():
    op_system = sys.platform
    if op_system == 'win32':
        subprocess.run('cls', shell=True)
    elif op_system == 'linux' or op_system == 'darwin':
        subprocess.run('clear', shell=True)

# This fuction is used to get the name of the customer
def getName():
    while True:
        print("")
        name = input("Card holder name: ").title()
        if name in customers:
            return name
        else:
            print("")
            print("Customer not found.")

# This function is used to make the menu
def getMenu():
    menu = [
        "Check Stock",
        "Shop",
        "Check Basket",
        "Modify Basket",
        "Check Out",
        "Account Details",
        "Exit"
    ]
    user_choice = 0
    while True:
        try:
            for index, value in enumerate(menu, start=1): 
                print(f"{index} :  {value}")
            print("")
            user_choice = int(input("Select an option (1-7): "))
            if 1 <= user_choice <=7:        
                return user_choice            
            else:
                print("\nPlease select 1 - 7\n")    
        except ValueError:
            print("Invalid. Please select 1-7")

# This function is used to check the stock
def checkStock():
    time.sleep(0.5) # Pauses for 0.5 seconds
    clearScreen()
    print("\n--------------------- In Store ----------------------")
    
    for i, (key, value) in enumerate(stock.items(), start=1):
        print(f"{i:>2}: {key:<37} - Qty: {value['qty']:<7} Price: ${value['price']:.2f}")
    print("")
    time.sleep(5)  # Pauses for 5 seconds

# This function is used to show the shop and things you can buy.
def shop():
    global basket 
    basket = {}
    time.sleep(0.5) # Pauses for 0.5 second
    clearScreen()
    print("\n--------------------- Shop ----------------------")
    for i, (key, value) in enumerate(stock.items(), start=1):
        print(f"{i:>2}: {key:<37} - Qty: {value['qty']:<7} Price: ${value['price']:.2f}")
    print("")
    
    # Loop to add specififc items to the basket with quantities and the option to return to the main menu
    print("Select the item number to add to your basket or type '0' to return to the main menu.")
    users_choice = input("Please select an item: ")
    while True:
        if users_choice == '0':
            print("")
            print("Returning to the main menu...")
            time.sleep(5)  # Pauses for 5 seconds
            clearScreen()
            break
        
        elif users_choice.isdigit() and 1 <= int(users_choice) <= len(stock):
            item_index = int(users_choice) - 1
            item_name = list(stock.keys())[item_index]
            item_qty = stock[item_name]['qty']
            
            
            quantity = input(f"Enter quantity for {item_name} (Available: {item_qty}): ")
            if quantity.isdigit() and 1 <= int(quantity) <= item_qty:
                
                print(f"Added {quantity} of {item_name} to your basket.")
                print("")
                
                if item_name in basket:
                    basket[item_name] += int(quantity)
                else:
                    basket[item_name] = int(quantity)

                stock[item_name]['qty'] -= int(quantity)
            else:
                print("Invalid quantity. Please try again.")
                print("")
        else:
            print("Invalid choice. Please try again.")
            print("")
        
        users_choice = input("Please select an item, or enter 0 to return to menu: ")
    
        
    time.sleep(5)  # Pauses for 5 seconds
    pass

basket = {}  # This initialize the basket as an empty dictionary

# This function is used to display the contents of the user's basket including the items, quantities, and total cost
def checkBasket():
    clearScreen()
    global basket
    
    print("Loading ... ")
    time.sleep(1)  # Pauses for 1 second
    clearScreen()
    
    print("\n--------------------- Basket ----------------------")
    print(f"{'Item: ':<37} {'Qty: ':<7} {'Price:':<10}")
    if not basket:
        print("Your basket is empty.")
        print("")
        return
    
    for i, (item, qty) in enumerate(basket.items(), start = 1):
        print(f"{i:>2} {item:<37} {qty:<7} ${stock[item]['price'] * qty:.2f}")
    total_price = sum(stock[item]['price'] * qty for item, qty in basket.items())
    print(f"\nTotal Price: ${total_price:.2f}")
    print("")
     
# This function is used to modify the contents of the user's basket
def modify():
    global basket

    while True:
        clearScreen()
        print("\n--------------------- Modify Basket ----------------------")

        if not basket:
            print("Your basket is empty.")
            return

        for i, (item, quantity) in enumerate(basket.items(), start=1):
            price = stock[item]["price"]
            print(f"{i}: {item} - Qty: {quantity} - Price: ${price * quantity:.2f}")
            #This calculates the total cost of the items in the basket
        total_cost = sum(stock[item]["price"] * quantity for item, quantity in basket.items())
        print(f"\nTotal Cost: ${total_cost:.2f}")

        choice = input("\nEnter item number to modify, or '0' to return to the menu: ")

        if choice == "0":
            return

        if not choice.isdigit() or not 1 <= int(choice) <= len(basket):
            print("Invalid item number.")
            continue

        item = list(basket.keys())[int(choice) - 1]
        new_quantity = input(
            f"Enter new quantity for '{item}' (0 to remove): "
        )

        if not new_quantity.isdigit():
            print("Please enter a valid quantity.")
            continue

        new_quantity = int(new_quantity)

        if new_quantity > stock[item]["qty"]:
            print("That quantity is not available.")
        elif new_quantity == 0:
            del basket[item]
            print(f"'{item}' removed from your basket.")
        else:
            basket[item] = new_quantity
            print(f"'{item}' quantity updated.")
            print(" ")

# This function is used to let the user checkout there basket
def checkOut():
    clearScreen()
    print("\n--------------------- Checkout ----------------------")
    if not basket:
        print("Your basket is empty, please continue shopping.")
        print("")
        return
    
    for i, (item, qty) in enumerate(basket.items(), start = 1):
        print(f"{i:>2} {item:<37} {qty:<7} ${stock[item]['price'] * qty:.2f}")
    
    # This calculates the total price of all the products
    total_price = sum(stock[item]['price'] * qty for item, qty in basket.items())
    print(f"\nTotal Price: ${total_price:.2f}")
    
    # Now we ask the user if they want to proceed with checkout or exit
    proceed = input("\nDo you want to proceed with checkout? (yes/no): ").strip().lower()
    if proceed == "no":
        print("\nReturning to the main menu...")
        time.sleep(1.5)
        clearScreen()
        return  # Exit the checkout process
    
    #This checks if the user has enough money in their account to purchase the items in their basket
    if getName() == "Joe Blogg":
        if customers['Joe Blogg']['Account'] >= total_price:
            customers['Joe Blogg']['Account'] -= total_price
            print(f"\nPurchase successful! Your new account balance is: ${customers['Joe Blogg']['Account']:.2f}")
            basket.clear() # This clears the basket after purchase is succesful
        else:
            print("\nInsufficient funds. Please remove some items from your basket.")
            
    elif getName() == "Matthew Jones":
        if customers['Matthew Jones']['Account'] >= total_price:
            customers['Matthew Jones']['Account'] -= total_price
            print(f"\nPurchase successful! Your new account balance is: ${customers['Matthew Jones']['Account']:.2f}")
            basket.clear() # This clears the basket after purchase is succesful
        else:
            print("\nInsufficient funds. Please remove some items from your basket.")
            
    elif getName() == "Wayne Aquila":
        if customers['Wayne Aquila']['Account'] >= total_price:
            customers['Wayne Aquila']['Account'] -= total_price
            print(f"\nPurchase successful! Your new account balance is: ${customers['Wayne Aquila']['Account']:.2f}")
            basket.clear() # This clears the basket after purchase is succesful
        else:
            print("\nInsufficient funds. Please remove some items from your basket.")
    
    elif getName() == "Elijah Paul":
        if customers['Elijah Paul']['Account'] >= total_price:
            customers['Elijah Paul']['Account'] -= total_price
            print(f"\nPurchase successful! Your new account balance is: ${customers['Elijah Paul']['Account']:.2f}")
            basket.clear() # This clears the basket after purchase is succesful
        else:
            print("\nInsufficient funds. Please remove some items from your basket.")
    print("")
    pass

# This function is used to call up the user's account details including their name, card number
def account():
    time.sleep(0.5) # Pauses for 0.5 seconds
    clearScreen()
    print("\n--------------------- Account Details ----------------------")
    if getName() == "Joe Blogg":
        time.sleep(0.5)
        print("")
        print("Welcome Joe Blogg, here are your account details:")
        print(f"Visa: {customers['Joe Blogg']['Visa']}")
        print(f"CVV: {customers['Joe Blogg']['CVV']}")
        print(f"Expiry: {customers['Joe Blogg']['Expiry']}")
        print(f"Account Balance: ${customers['Joe Blogg']['Account']:.2f}")
        print(f"Username: {customers['Joe Blogg']['Username']}")
        print(f"Email: {customers['Joe Blogg']['Email']}")
        print(f"Mobile: {customers['Joe Blogg']['Mobile']}")
        print(f"Street: {customers['Joe Blogg']['Street']}")
        print(f"Suburb: {customers['Joe Blogg']['Suburb']}")
        print(f"City: {customers['Joe Blogg']['City']}")
        print(f"Area Code: {customers['Joe Blogg']['Area Code']}")
        print("")
        time.sleep(2)  # Pauses for 2 seconds
    
    elif getName() == "Matthew Jones":
        time.sleep(0.5) # Pauses for 0.5 seconds
        print("")
        print("Welcome Matthew Jones, here are your account details:")
        print(f"Visa: {customers['Matthew Jones']['Visa']}")
        print(f"CVV: {customers['Matthew Jones']['CVV']}")
        print(f"Expiry: {customers['Matthew Jones']['Expiry']}")
        print(f"Account Balance: ${customers['Matthew Jones']['Account']:.2f}")
        print(f"Username: {customers['Matthew Jones']['Username']}")
        print(f"Email: {customers['Matthew Jones']['Email']}")
        print(f"Mobile: {customers['Matthew Jones']['Mobile']}")
        print(f"Street: {customers['Matthew Jones']['Street']}")
        print(f"Suburb: {customers['Matthew Jones']['Suburb']}")
        print(f"City: {customers['Matthew Jones']['City']}")
        print(f"Area Code: {customers['Matthew Jones']['Area Code']}")
        print("")
        time.sleep(2)  # Pauses for 2 seconds
    
    elif getName() == "Wayne Aquila":
        time.sleep(0.5) # Pauses for 0.5 seconds
        print("")
        print("Welcome Wayne Aquila, here are your account details:")
        print(f"Visa: {customers['Wayne Aquila']['Visa']}")
        print(f"CVV: {customers['Wayne Aquila']['CVV']}")
        print(f"Expiry: {customers['Wayne Aquila']['Expiry']}")
        print(f"Account Balance: ${customers['Wayne Aquila']['Account']:.2f}")
        print(f"Username: {customers['Wayne Aquila']['Username']}")
        print(f"Email: {customers['Wayne Aquila']['Email']}")
        print(f"Mobile: {customers['Wayne Aquila']['Mobile']}")
        print(f"Street: {customers['Wayne Aquila']['Street']}")
        print(f"Suburb: {customers['Wayne Aquila']['Suburb']}")
        print(f"City: {customers['Wayne Aquila']['City']}")
        print(f"Area Code: {customers['Wayne Aquila']['Area Code']}")
        print("")
        time.sleep(2)  # Pauses for 2 seconds
        
    elif getName() == "Elijah Paul":
        time.sleep(0.5) # Pauses for 0.5 seconds
        print("")
        print("Welcome Elijah Paul, here are your account details:")
        print(f"Visa: {customers['Elijah Paul']['Visa']}")
        print(f"CVV: {customers['Elijah Paul']['CVV']}")
        print(f"Expiry: {customers['Elijah Paul']['Expiry']}")
        print(f"Account Balance: ${customers['Elijah Paul']['Account']:.2f}")
        print(f"Username: {customers['Elijah Paul']['Username']}")
        print(f"Email: {customers['Elijah Paul']['Email']}")
        print(f"Mobile: {customers['Elijah Paul']['Mobile']}")
        print(f"Street: {customers['Elijah Paul']['Street']}")
        print(f"Suburb: {customers['Elijah Paul']['Suburb']}")
        print(f"City: {customers['Elijah Paul']['City']}")
        print(f"Area Code: {customers['Elijah Paul']['Area Code']}")
        print("")
        time.sleep(2)  # Pauses for 2 seconds
    
    else:
        print("Customer not found.")
        time.sleep(2)
        clearScreen()
        
# This function is used to get rid of everything as they are done
def exit():
    clearScreen()
    print("")
    pass

