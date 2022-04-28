import Cart
"""
import User
import Inventory
import Book"""
import sys
import os

# pre-login looping menu
def preLoginLoop():
    try:
        choice = int(input("1. Login\n2. Create Account\n3. Exit"))
        if choice == 1:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            found = False
            # opens user file
            userfile = open("users.txt", "r")
            # loops through file to find if user is in file
            # if the user is found and password is correct, it will send them to postLoginLoop
            for line in userfile:
                usertemp = line.split(", ")
                if usertemp == username:
                    passtemp = line.split(", ")
                    if passtemp == password:
                        found = True
                        break
            userfile.close()
            # if found, welcomes user and starts main menu
            if found == True:
                print("Welcome " + username)
                return (True, username)
            else:
                print("Error logging in... Make sure your credentials are corrrect.\n")
                print("If you do not have an account enter 3 to make one now.")
        elif choice == 2:
            while(True):
                newUsername = input("Enter your desired username: ")
                # checks to see if username is available and makes them create new one if it exists
                checkfile = open("users.txt", "r")
                for line in checkfile:
                    usertemp = line.split(", ")
                    if usertemp == newUsername:
                        print("Username already exists...")
                    else:
                        newPassword = input("Enter your desired password: ")
                        print("Let's finish setting up your account...\n")
                        newFirstName = input("First name: ")
                        newLastName = input("Last name: ")
                        print("Enter your payment info: \n")
                        newCardNum = input("\tCredit Card number: ")
                        newExpDate = input("\tExpiration Date: ")
                        newSecCode = input("\tSecurity code: ")
                        print("Enter your billing/shipping information: ")
                        newAddress = input("\tStreet: ")
                        newCity = input("\tCity: ")
                        newState = input("\tState: ")
                        newZip = input("\tZip Code: ")

                        userfile = open("userfile.txt", "a")
                        userfile.write(newUsername, ", ", newPassword, ", ", newFirstName, ", ",newLastName, ", ",newCardNum, ", ", newExpDate, ", ", newSecCode, ", ", newAddress, ", ", newCity, ", ", newState, ", ", newZip)
                        print("User created successfully!")
                        return(True, newUsername)
        elif choice == 3:
            sys.exit()
        else:
            print("Pick an option by selecting a number 1-3")
            return False, "no"
    except:
        print("Enter a number 1-3")
        return False, "no"

def postLoginLoop(username):
    
    try:
        choice = int(input("Select One of the following:\n1. View Books\n2. View Cart\n3. View Profile\n4. Logout\n5. Exit Program"))
        if choice == 1:
            # display book list with info, then three options: add book to cart, view cart, return to menu
            
            ### display books here
            
            opt = int(input("Select an option:\n1. Add item to Cart\n2. View Cart\n3. Return to Menu"))
            if opt == 1:
                
            elif opt == 2:
                viewCart()
            elif opt == 3:
                preLoginLoop(username)
        elif choice == 2:
            # display cart and total, then three options: edit cart, checkout, return to menu
            viewCart()
        elif choice == 3:
            # display basic info like name and user name, then four options: Edit info, view order history, delete account, return to menu
        elif choice == 4:
            preLoginLoop(username)
        elif choice == 5:
            sys.exit()
        else:
            print("That was not a valid option...")
            preLoginLoop(username)
    except: 
        print("That was not a valid option...")
        preLoginLoop(username)

# loop through cart books and display info
def viewCart():
    ISBNs = Cart.getISBNs()
    qtys = Cart.getQTYs()
    
    ## loop through inventory to get appropraite info, then print it all out
    
    num = int(input("1. Remove Item(s)\n2. Checkout\n3. Return to Menu"))
    
    if num == 1:
        try:
            isbnDelInd = int(input("Which item would you like to remove?"))
            qtyDelNum = int(input("How many would you like to remove?"))
            

        except:
            "An error occurred. Please check the information you entered and try again..."
            viewCart()
    elif num == 2:
        checkout()
    elif num == 3:
        postLoginLoop(user)
    else:
        print("Error, Try again.")
        viewCart()
        
def checkout():
    
    
#main
# create instnace of Inventory, Cart, User
print("Welcome to the Group 11 Bookstore. Please login or create an account: \n")
while(True):
    x, user = preLoginLoop()
    if(x):
        postLoginLoop(user)
