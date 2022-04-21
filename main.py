import Cart
import User
import Inventory
import Book

import os

# pre-login looping menu
def preLoginLoop():

    while(cont == True):
        try:
            choice = int(input("1. Login\n2. Create Account\n3. Exit"))
            if choice == 1:
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                found = false
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
                if found == true:
                    print("Welcome " + username)
                    postLoginLoop()
                else:
                    print("Error logging in... Make sure your credentials are corrrect.\n")
                    print("If you do not have an account enter 3 to make one now.")
            else if choice == 2:
                while(True):
                    newUsername = input("Enter your desired username: ")
                    # checks to see if username is available and makes them create new one if it exists
                    checkfile = open("users.txt", "r")
                    for line in checkfile:
                        usertemp = line.split(", ")
                        if usertemp == newUsername:
                            print("Username already exists...")
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
            else if choice == 3:
                cont = False
            else:
                print("Pick an option by selecting a number 1-3")
        except:
            print("Enter a number 1-3")

def postLoginLoop():


#main
print("Welcome to the Group 11 Bookstore. Please login or create an account: \n")
preLoginLoop()
