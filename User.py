# this will be the user class
from errno import ECONNREFUSED
from multiprocessing.sharedctypes import Value
from sre_parse import expand_template
import os

class User:

    def __init__(self):
        self.__username = ""  # str
        self.__password = ""  # str
        self.__firstName = ""  # str
        self.__lastName = ""  # str
        self.__cardNum = 0  # int
        self.__expDate = ""  # str
        self.__secCode = 0  # int
        self.__address = []  # str(list)
        self.__orderHist = []  # Cart

    def setUname(self, Uname):
        self.__username = Uname

    def setPass(self, pWord):
        self.__password = pWord

    def setFName(self, fName):
        self.__firstName = fName

    def setLName(self, lName):
        self.__lastName = lName

    def setOrderHist(self, orderList):
        for x in orderList:
            self.__orderHist.append(x)

    # appends new user or updated info to end of file. Old line will need to be deleted.
    def prepLine(self):
        # ready the address for new input
        # address line-city-state-zip
        line = str(self.__address[0])
        city = str(self.__address[1])
        state = str(self.__address[2])
        zip = str(self.__address[3])
        tmpAdd = line + "-" + city + "-" + state + "-" + zip

        print(self.__orderHist)
        # ready history to be stored
        i = 0
        length = len(self.__orderHist)
        tmpHist = ""
        while i < length:
            if tmpHist == "":
                tmpHist = str(self.__orderHist[i])
            else:
                tmpHist = tmpHist + "-" + str(self.__orderHist[i])
            i = i + 1

        # ready expiration date
        tmpExp = self.__expDate[0] + "-" + self.__expDate[1]

        print(self.__expDate)
        uname = str(self.__username)
        pword = str(self.__password)
        fname = str(self.__firstName)
        lname = str(self.__lastName)
        cardN = str(self.__cardNum)
        expD = str(self.__expDate)
        secC = str(self.__secCode)

        string1 = uname + ", " + pword + ", " + fname + ", " + lname
        string2 = string1 + ", " + cardN + ", <" + tmpExp + ">, " + secC
        finalString = string2 + ", <" + tmpAdd + ">, <" + tmpHist + ">"

        with open("users.txt", "a+") as file_object:
            # Move read cursor to the start of file.
            file_object.seek(0)
            # If file is not empty then append '\n'
            data = file_object.read(100)
            if len(data) > 0:
                file_object.write("\n")
            # Append text at the end of file
            file_object.write(finalString)

    def getFname(self):
        return self.__firstName

    def getLname(self):
        return self.__lastName

    def getPay(self):  # int - read off the various
        return [self.__cardNum, self.__expDate, self.__secCode]

    # takes in new card info, be it for a new user or a person changing their card.
    # utilizes try/excepts to catch unacceptable answers and loops until all conditions are met
    # expiration should be entered as a list
    def setPay(self, number, expiration, securityCode):
        self.__cardNum = number
        self.__expDate = expiration
        self.__secCode = securityCode

    def getAdd(self):  # str
        print("Retrieving address...")
        return self.__address

    def setAdd(self, street, city, state, zip):
        tempAdd = [street, city, state, zip]
        self.__address = tempAdd

    # will be a using the list of order history, which will comprise of the cart IDs to get access to the histories
    # stored in the cart.py file
    def getHist(self):  # void
        print("Retrieving previous cart IDs...")
        return self.__orderHist

    def getUName(self):
        return self.__username

    # lines is the complete list of read lines in the users.txt files
    # userLine is the index number for the line containing active user's information
    def delProfile(self):  # Bool

        here = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(here, 'users.txt')

        fp = open(filename, "r+")

        lines = fp.readlines()
        userLine = -1
        x = 0
        while x < len(lines):
            thisUname = lines[x].split(", ")[0]
            if self.__username == thisUname:
                userLine = x
                break
            else:
                x += 1

        if userLine != -1:
            fp.seek(0, 0)
            fp.truncate(0)
            for number, line in enumerate(lines):
                if number not in [userLine]:
                    fp.write(line)

        print("Profile successfully deleted. Have a wonderful life! ^-^")
        fp.close()

    def commit_to_file(self):
        deli = ", "

        expDateWrite = self.__expDate
        expDateWrite = expDateWrite.replace("/", "-")

        expDateWrite = "".join(("<", expDateWrite, ">"))

        addToWrite = "<" + self.__address[0] + "-" + self.__address[1] + "-" + self.__address[2] + "-" + self.__address[3] + ">"

        orderHistWrite = "<"
        if len(self.__orderHist) > 0:
            for x in self.__orderHist:
                orderHistWrite += str(x)
                orderHistWrite += "-"
            orderHistWrite = orderHistWrite[:-1]
        orderHistWrite += ">"

        here = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(here, 'users.txt')

        userFile = open(filename, "a")
        userFile.write("\n" + self.__username + deli + self.__password + deli + self.__firstName + deli + self.__lastName +
                       deli + str(self.__cardNum) + deli + expDateWrite + deli + str(self.__secCode) + deli +
                       addToWrite + deli + orderHistWrite)

        userFile.close()



# functions reads through file and adds everything toa list.
def prepUser(index):
    lines = []

    # reads each line into a list of lines
    with open('users.txt') as f:
        lines = f.readlines()

    # Upon finding the line number/matching index, use that same number to remove commas
    nocomma = []
    nocomma = lines[index].split(', ')

    return nocomma, lines


def prepULists(nocomma):
    # finishes setting up address
    addBreak = []
    addBreak = nocomma[7].split('-')
    nocomma[7] = addBreak

    # sets up orderHistory
    orderBreak = []
    orderBreak = nocomma[9].split('-')
    nocomma[9] = orderBreak
    temp = orderBreak[2]
    tempdone = temp[:-1]
    orderBreak[2] = tempdone

    # sets up expeiration date into a small two index-long list
    expBreak = []
    expBreak = nocomma[5].split('-')
    nocomma[5] = expBreak

    return nocomma





'''
1. Read users.txt into a list, each index containing one whole line of info. (save lines and index where line is
found)
2. Find user info needed and proceed to format for the main program to use. Will include function used.
3.Cases for various scenarios:
    Changing/setting address or payment info:
        testInstance.setAdd(street, city, state, zip)
        #OR 
        testInstance.setPay(number, expiration, securityCode)
        testInstance.delProfile(lines, index) - deletes old info
        testUnit.prepLine() - appends new info onto a new line
'''