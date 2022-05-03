from Cart import Cart
from User import User
from Inventory import Inventory
from Book import Book
import sys
import os


# pre-login looping menu
def preLoginLoop():
    try:
        choice = int(input("1. Login\n2. Create Account\n3. Exit\n"))
        if choice == 1:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            found = False
            # opens user file
            userfile = open("users.txt", "r")
            # loops through file to find if user is in file
            # if the user is found and password is correct, it will send them back to main

            fnameTemp = ""
            lnameTemp = ""
            cardNTemp = 0
            eDate = ""
            secCodeTemp = 0
            addTemp = ""
            orderHist = ""
            orderHistList = []
            # ---------------Double check this with user file template
            for line in userfile:
                usertempInfo = line.split(", ")
                if usertempInfo[0] == username:
                    passtemp = usertempInfo[1]
                    if passtemp == password:
                        fnameTemp = usertempInfo[2]
                        lnameTemp = usertempInfo[3]
                        cardNTemp = usertempInfo[4]
                        eDate = usertempInfo[5]
                        # next two lines remove brackets from eDate
                        # Used delft stack website for string slicing code
                        eDate = eDate[:-1]
                        eDate = eDate[1:]
                        secCodeTemp = usertempInfo[6]
                        addTemp = usertempInfo[7]
                        orderHist = usertempInfo[8]
                        orderHist = orderHist.replace("<", "")
                        orderHist = orderHist.replace(">", "")
                        orderHist = orderHist[:-1]
                        orderHistList = orderHist.split("-")

                        found = True
                        break
            userfile.close()
            # if found, welcomes user and starts main menu
            if found:
                yourUser = User()
                yourUser.setUname(username)
                yourUser.setPass(password)
                yourUser.setFName(fnameTemp)
                yourUser.setLName(lnameTemp)
                yourUser.setPay(cardNTemp, eDate, secCodeTemp)
                addTuple = addTemp.split("-")
                yourUser.setAdd(addTuple[0], addTuple[1], addTuple[2], addTuple[3])
                if len(orderHistList) > 0:
                    yourUser.setOrderHist(orderHistList)
                print("Welcome " + yourUser.getUName())
                return True, yourUser
            else:
                print("Error logging in... Make sure your credentials are correct.\n")
                print("If you do not have an account enter 2 to make one now.")
                blankuser = User()
                return False, blankuser
        elif choice == 2:
            while True:
                newUsername = input("Enter your desired username: ")
                # checks to see if username is available and makes them create new one if it exists
                checkfile = open("users.txt", "r")
                alreadyExists = False
                for line in checkfile:
                    usertempLine = line.split(", ")
                    if usertempLine[0] == newUsername:
                        alreadyExists = True
                if alreadyExists:
                    print("Username already exists...")
                else:
                    newPassword = input("Enter your desired password: ")
                    print("Let's finish setting up your account...\n")
                    newFirstName = input("First name: ")
                    newLastName = input("Last name: ")
                    print("Enter your payment info: \n")
                    newCardNum = input("\tCredit Card number: ")
                    newExpDate = input("\tExpiration Date (MM/YY): ")
                    newSecCode = input("\tSecurity code: ")
                    print("Enter your billing/shipping information: ")
                    newAddress = input("\tStreet: ")
                    newCity = input("\tCity: ")
                    newState = input("\tState: ")
                    newZip = input("\tZip Code: ")

                    newUser = User()
                    newUser.setUname(newUsername)
                    newUser.setPass(newPassword)
                    newUser.setFName(newFirstName)
                    newUser.setLName(newLastName)
                    newUser.setPay(newCardNum, newExpDate, newSecCode)
                    newUser.setAdd(newAddress, newCity, newState, newZip)
                    newUser.commit_to_file()
                    print("User created successfully!")
                    return True, newUser
        elif choice == 3:
            ExitUser = User()
            ExitUser.setUname("Exit_Program")
            print("\nGoodbye!")
            return True, ExitUser
        else:
            print("Pick an option by selecting a number 1-3")
            blankUser = User()
            return False, blankUser
    except:
        print("Enter a number 1-3")
        blankUser = User()
        return False, blankUser


# loop through cart books and display info
def viewCart(yourCart, book_list):
    ISBNs = yourCart.getISBNs()
    qtys = yourCart.getQTYs()

    if len(ISBNs) == 0:
        print("Your cart is empty!")
        return 3
    # loop through inventory to get appropriate info, then print it all out
    z = 0
    while z < len(ISBNs):
        for y in book_list:
            if ISBNs[z] == y.get_isbn():
                print(str(z + 1) + ". " + str(qtys[z]) + " copies of " + y.get_title() + " by " + y.get_author())
        z += 1

    print("Current Total: $" + "{:.2f}".format((yourCart.getCurrentTotal())))

    num = int(input("1. Remove Item(s)\n2. Checkout\n3. Back\n"))
    # loops to make sure valid option
    while num != 1 and num != 2 and num != 3:
        num = int(input("1. Remove Item(s)\n2. Checkout\n3. Back\n"))
    return num


def postLoginMenu():
    choice = int(input("Select One of the following:\n1. View Books\n2. View Cart\n3. View Profile\n4. Logout\n5. "
                       "Exit Program\n"))
    return choice


def viewBookMenu():
    choice = int(input("Select an option:\n1. Add item to Cart\n2. View Cart\n3. Return to Menu\n"))
    return choice


# main
def main():
    # create instance of Inventory, booklist
    our_inv = Inventory()
    book_list = []
    # adds books to book list using isbn's from inventory
    for x in our_inv.get_isbns():
        y = Book(x)
        book_list.append(y)
    print("Welcome to the Group 11 Bookstore. Please login or create an account: ")
    while True:
        yourUser = User()
        x = False
        while not x:
            x, yourUser = preLoginLoop()
        # checks for exit option
        if yourUser.getUName() == "Exit_Program":
            sys.exit()
        # work on instance of user, and then cart instance will be fixed
        yourCart = Cart(yourUser.getUName())
        while x:
            try:
                # main loop options----
                num1 = postLoginMenu()
                if num1 == 1:
                    contBookMenu = True
                    while contBookMenu:
                        # displays books, author, and price
                        i = 0
                        while i < len(book_list):
                            print(str(i + 1) + ". ",
                                  book_list[i].get_title() + " by " + book_list[i].get_author() + " - " + book_list[
                                      i].get_amount() + " copies priced at $" + book_list[i].get_price())
                            i += 1
                        opt = viewBookMenu()  # 1. add item to cart 2. view cart 3. return to menu
                        if opt == 1:
                            while 1:
                                try:
                                    bookChoice = int(
                                        input("Which book would you like to add to your cart? (Enter item number...)"))
                                    qtyChoice = int(input("How many would you like to add?\n"))
                                    # check to make sure valid input
                                    isbnChoice = book_list[bookChoice - 1].get_isbn()
                                    priceChoice = book_list[bookChoice - 1].get_price()
                                    yourCart.addItem(isbnChoice, qtyChoice, priceChoice)  # adds given item to cart
                                    our_inv.edit_qty(isbnChoice, qtyChoice)  # decrease inventory here
                                    for p in book_list:  # this loops and decreases amount from book in book list
                                        if p.get_isbn() == isbnChoice:
                                            p.reduce_amount(qtyChoice)
                                            break
                                    break
                                except:
                                    print("An error occurred; try again.")
                        elif opt == 2:
                            contCartMenu = True
                            while contCartMenu:
                                choice = viewCart(yourCart, book_list)

                                if choice == 1:
                                    # remove items from cart
                                    isbnDelInd = int(input("Which item would you like to remove?")) - 1
                                    isbnDel = book_list[isbnDelInd].get_isbn()
                                    qtyDelNum = int(input("How many would you like to remove?"))
                                    # remove from cart, add back to inventory and booklist
                                    this_price = book_list[isbnDelInd].get_price()
                                    yourCart.remItem(isbnDel, qtyDelNum, this_price)
                                    book_list[isbnDelInd].increase_amount(qtyDelNum)
                                    our_inv.edit_qty(isbnDel, -qtyDelNum)

                                elif choice == 2:  # checkout option
                                    # displays cart contents
                                    print("Your total is: $" + str(yourCart.getCurrentTotal()) + "\n")
                                    lastFour = str(str(yourUser.getPay()[0][-4:-1]) + str(yourUser.getPay()[0][-1]))
                                    print("Using card ending in " + lastFour)

                                    print("Thanks for your purchase!")

                                    ISBNs = yourCart.getISBNs()
                                    QTYs = yourCart.getQTYs()

                                    for x in book_list:
                                        if x.get_isbn() in ISBNs:
                                            x.reduce_amount(int(QTYs[ISBNs.index(x.get_isbn())]))

                                    yourUser.setOrderHist([yourCart.getCartId()])

                                    yourCart.commitToFile()
                                    yourCart = Cart(yourUser.getUName())

                                    # deletes file and recreates with updates information
                                    os.remove("inventory.txt")
                                    here = os.path.dirname(os.path.abspath(__file__))
                                    filename = os.path.join(here, 'inventory.txt')
                                    f = open(filename, "x")
                                    for x in book_list:
                                        our_inv.commit_book_to_file(x.get_isbn(), x.get_title(), x.get_author(),
                                                                    x.get_genre(), x.get_amount(), x.get_price())

                                    contCartMenu = False
                                elif choice == 3:
                                    contCartMenu = False
                        elif opt == 3:
                            # back to menu, not sure anything has to be put here? check back
                            contBookMenu = False

                elif num1 == 2:
                    contCartMenu = True
                    while contCartMenu:
                        opt = viewCart(yourCart, book_list)

                        if opt == 1:
                            # remove items from cart
                            isbnDelInd = int(input("Which item would you like to remove?")) - 1
                            isbnDel = book_list[isbnDelInd].get_isbn()
                            qtyDelNum = int(input("How many would you like to remove?"))
                            # remove from cart, add back to inventory and booklist
                            this_price = book_list[isbnDelInd].get_price()
                            yourCart.remItem(isbnDel, qtyDelNum, this_price)
                            book_list[isbnDelInd].increase_amount(qtyDelNum)
                            our_inv.edit_qty(isbnDel, -qtyDelNum)

                        elif opt == 2:  # checkout option
                            # displays cart contents
                            print("Your total is: $" + str(yourCart.getCurrentTotal()) + "\n")
                            lastFour = str(str(yourUser.getPay()[0][-4:-1]) + str(yourUser.getPay()[0][-1]))
                            print("Using card ending in " + lastFour)

                            print("Thanks for your purchase!")

                            ISBNs = yourCart.getISBNs()
                            QTYs = yourCart.getQTYs()

                            for x in book_list:
                                if x.get_isbn() in ISBNs:
                                    x.reduce_amount(int(QTYs[ISBNs.index(x.get_isbn())]))

                            yourUser.setOrderHist([yourCart.getCartId()])

                            yourCart.commitToFile()
                            yourCart = Cart(yourUser.getUName())

                            # deletes file and recreates with updates information
                            os.remove("inventory.txt")
                            here = os.path.dirname(os.path.abspath(__file__))
                            filename = os.path.join(here, 'inventory.txt')
                            f = open(filename, "x")
                            for x in book_list:
                                our_inv.commit_book_to_file(x.get_isbn(), x.get_title(), x.get_author(),
                                                            x.get_genre(), x.get_amount(), x.get_price())

                            contCartMenu = False
                        elif opt == 3:
                            contCartMenu = False

                elif num1 == 3:  # view profile
                    contProfMenu = True
                    while contProfMenu:

                        # display basic info like name and user name, then four options:
                        # Edit info, view order history, delete account, back
                        print("username: " + yourUser.getUName())
                        print("Name: " + yourUser.getFname() + " " + yourUser.getLname())
                        opt = int(input("1. Edit Personal Info\n2. View Order History\n3. Delete Account\n4. Back\n"))
                        # makes sure valid option
                        while opt != 1 and opt != 2 and opt != 3 and opt != 4:
                            print("Pick a valid option please...")
                            opt = int(
                                input("1. Edit Personal Info\n2. View Order History\n3. Delete Account\n4. Back\n"))

                        # Edit Info loop
                        if opt == 1:
                            editProfMenu = True
                            while editProfMenu:
                                editChoice = int(input("What would you like to edit?\n\t1. Name\n\t2. Payment "
                                                       "Information\n\t3. Address\nOr press 4 to go back"))
                                # new name option
                                if editChoice == 1:
                                    fname = str(input("Enter your first name: "))
                                    lname = str(input("Enter your last name: "))
                                    yourUser.setFName(fname)
                                    yourUser.setLName(lname)

                                # new payment info
                                elif editChoice == 2:
                                    cardNum = int(input("Enter your card number: "))
                                    secCode = int(input("Enter your card's security code: "))
                                    expDate = str(input("Enter your card's expiration date (MM/YY): "))
                                    yourUser.setPay(cardNum, expDate, secCode)

                                # new address info
                                elif editChoice == 3:
                                    street = str(input("Enter you street address: "))
                                    city = str(input("City: "))
                                    state = str(input("State: "))
                                    zipCode = int(input("Zip code: "))
                                    yourUser.setAdd(street, city, state, zipCode)

                                elif editChoice == 4:  # Back
                                    editProfMenu = False
                                    yourUser.delProfile()
                                    yourUser.commit_to_file()
                                else:
                                    print("Not a valid choice... try again.")

                        # view order history
                        elif opt == 2:
                            prevOrders = yourUser.getHist()

                            # loop through each item in prevOrders
                            if len(prevOrders) == 0:
                                print("You have never completed an order with us.")

                            else:
                                cartFile = open("carts.txt", "r")
                                j = 0
                                while j < len(prevOrders):
                                    for line in cartFile:
                                        cartID, userID, price, ISBNlist, QTYlist = line.split(", ")
                                        if cartID == prevOrders[j]:
                                            print("Order ID #" + cartID)
                                            print("\tTotal: $" + price)
                                    cartFile.seek(0, 0)
                                    j += 1
                                # could add more info if have time
                                cartFile.close()


                        elif opt == 3:
                            # delete account
                            yourUser.delProfile()  # check back on arguments for this
                            contProfMenu = False
                            x = False
                            # check back on where to go in the menu from here

                        elif opt == 4:
                            contProfMenu = False
                elif num1 == 4:
                    print("Your changes will not be saved... See you next time!")
                    x = False  # sets overall variable to false to return to first while loop

                elif num1 == 5:
                    sys.exit()

                else:
                    print("Not a valid option... Try again")

            except SystemExit:
                print("Goodbye!")
                sys.exit()


if __name__ == "__main__":
    main()
