from data.customer import customers 
import sys, time, re, random, os, subprocess, shutil
from data.stock import stock
# from data.stock import stock

# Clear screen on window, linux, mac
def clearScreen():
    op_system = sys.platform
    if op_system == 'win32':
        subprocess.run('cls', shell=True)
    elif op_system == 'linux' or op_system == 'darwin':
        subprocess.run('clear', shell=True)

def getName():
    while True:
        print("")
        name = input("Card holder name: ").title()
        if name in customers:
            return name
        else:
            print("")
            print("Customer not found.")

# This function is fully working as inteded
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

def checkStock():
    time.sleep(0.5) # Pauses for 1 second
    clearScreen()
    print("\n--------------------- In Store ----------------------")
    
    for i, (key, value) in enumerate(stock.items(), start=1):
        print(f"{i:>2}: {key:<37} - Qty: {value['qty']:<7} Price: ${value['price']:.2f}")
    print("")
    time.sleep(40)  # Pauses for 40 seconds
    print("\nReturning to main menu...")
    clearScreen()

def shop():
    print("")
    pass

def checkBasket():
    print("")
    pass

def modify():
    print("")
    pass

def checkOut():
    print("")
    pass

def account():
    print("")
    pass

def exit():
    print("")
    pass

# # Clear screen on window, linux, mac
def clearScreen():
    op_system = sys.platform
    if op_system == 'win32':
        subprocess.run('cls', shell=True)
    elif op_system == 'linux' or op_system == 'darwin':
        subprocess.run('clear', shell=True)

