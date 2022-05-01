import Cart


import User
"""import Inventory"""
import Book
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
            if found:
                print("Welcome " + username)
                return True, username
            else:
                print("Error logging in... Make sure your credentials are correct.\n")
                print("If you do not have an account enter 3 to make one now.")
                preLoginLoop()
        elif choice == 2:
            while True:
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
                        userfile.write(newUsername, ", ", newPassword, ", ", newFirstName, ", ", newLastName, ", ",
                                       newCardNum, ", ", newExpDate, ", ", newSecCode, ", ", newAddress, ", ", newCity,
                                       ", ", newState, ", ", newZip)
                        print("User created successfully!")
                        return (True, newUsername)
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
        choice = int(input(
            "Select One of the following:\n1. View Books\n2. View Cart\n3. View Profile\n4. Logout\n5. Exit Program"))
        if choice == 1:
            # displays books, author, and price
            i = 0
            while i < len(bookList):
                print("Item " + (i + 1) + ". ",
                      bookList[i].getTitle() + " by " + bookList[i].getAuthor() + " - " + bookList[i].getPrice())
                i += i

            # then three options: add book to cart, view cart, return to menu

            opt = int(input("Select an option:\n1. Add item to Cart\n2. View Cart\n3. Return to Menu"))
            if opt == 1:
                while 1:
                    try:
                        bookChoice = int(input("Which book would you like to add to your cart? (Enter item number..."))
                        qtyChoice = int(input("How many would you like to add?"))
                        # check to make sure valid input
                        isbnChoice = bookList[bookChoice - 1].getISBN()
                        priceChoice = bookList[bookChoice - 1].getPrice()
                        yourCart.addItem(isbnChoice, qtyChoice, priceChoice)
                        ourInv.EditQty(isbnChoice, ) # decrease inventory here

                        break
                    except:
                        print("An error occurred, please try again")
            elif opt == 2:
                viewCart()
            elif opt == 3:
                preLoginLoop(username)
        elif choice == 2:
            # display cart and total, then three options: edit cart, checkout, return to menu
            viewCart()
        elif choice == 3:
            # display basic info like name and user name, then four options:
            # Edit info, view order history, delete account, return to menu
            print("username: " + yourUser.getUsername())
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
    ISBNs = yourCart.getISBNs()
    qtys = yourCart.getQTYs()

    # loop through inventory to get appropriate info, then print it all out
    x = 0
    while x < len(ISBNs):
        for y in bookList:
            if ISBNs[x] == y.getISBN():
                print(qtys[x] + "copies of " + y.getTitle() + " by " + y.getAuthor())
        x += x
    print("Current Total: $" + yourCart.getCurrentTotal())

    num = int(input("1. Remove Item(s)\n2. Checkout\n3. Return to Menu"))

    if num == 1:
        try:
            isbnDelInd = int(input("Which item would you like to remove?"))
            qtyDelNum = int(input("How many would you like to remove?"))
            yourCart.removeItem(isbnDelInd, qtyDelNum, )
        except:
            "An error occurred. Please check the information you entered and try again..."
            viewCart()
    elif num == 2:
        yourCart = checkout(yourCart)
        postLoginLoop(yourUser)
    elif num == 3:
        postLoginLoop(user)
    else:
        print("Error, Try again.")
        viewCart()


def checkout(yourCart):
    print("Your total is: $" + yourCart.getCurrentTotal() + "\n")
    print("Using card ending in " + yourUser.getPay())
    yourCart.commitToFile()
    yourCart = Cart()
    return yourCart



# main
# create instance of Inventory, booklist
ourInv = Inventory()
bookList = []
# adds books to book list using isbns from inventory
for x in ourInv.getISBNs():
    y = Book(x)
    bookList.append(y)
print("Welcome to the Group 11 Bookstore. Please login or create an account: \n")
while True:
    x, user = preLoginLoop()
    if x:
        yourCart = Cart()
        yourUser = User()
        postLoginLoop(user)
