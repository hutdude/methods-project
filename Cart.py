import os


class Cart:

    def __init__(self, Customer_id):
        self.Customer_id = Customer_id

        here = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(here, 'carts.txt')

        cartfile = open(filename, "r")
        # initilizes cart id variable at 1 and adds one for every existing cart id, makes new cart_id one more than current number
        counter = 1
        for line in cartfile:
            counter += 1

        # makes sure cart_ids are four characters long
        self.Cart_id = str(counter).zfill(4)

        cartfile.close()
        self.ISBNs = []
        self.qtys = []

        self.currentTotal = 0.00

    def addItem(self, ISBN, qty, price):
        # checks to see if ISBN already exists in cart. If it does, simply adds the given qty to current
        for x in self.ISBNs:
            if x == ISBN:
                self.qtys[self.ISBNs.index(x)] = self.qtys[self.ISBNs.index(x)] + qty
                return
        # if not, adds new isbn to list as well as qty, adjusts cart's current total
        self.ISBNs.append(ISBN)
        self.qtys.append(qty)
        self.currentTotal = self.currentTotal + price * qty

    def remItem(self, ISBN, qty, price):
        for x in self.ISBNs:
            if x == ISBN:
                # checks to make sure qty is a valid amount
                if qty < self.qtys[self.ISBNs.index(x)]:
                    self.qtys[self.ISBNs.index(x)] = self.qtys[self.ISBNs.index(x)] - qty
                    self.currentTotal = self.currentTotal - qty * price
                    return True
                elif qty == self.qtys[self.ISBNs.index(x)]:
                    del self.qtys[self.ISBNs.index(x)]
                    del self.ISBNs[self.ISBNs.index(x)]
                    self.currentTotal = self.currentTotal - qty * price
                    return True
                else:
                    return False
        return False

    def getCartId(self):
        return self.Cart_id

    def getCSTid(self):
        return self.Customer_id

    def getISBNs(self):
        return self.ISBNs

    def getQTYs(self):
        return self.qtys

    def getCurrentTotal(self):
        return self.currentTotal

    def commitToFile(self):
        # opens file
        cartfile = open("cars.txt", "a")
        # writes cart_id, customer_id, price
        cartfile.write(str(self.Cart_id) + ", " + str(self.Customer_id) + ", " + str(self.currentTotal) + ", ")

        # loops through isbn list and writes them to file and doesn't add delimeter after
        for x in self.ISBNs:
            if self.ISBNs.index(x) == len(self.ISBNs) - 1:
                cartfile.write(x + ", ")
            cartfile.write(x + ":")

        # loops through qtys list and writes them to file, accounts for the last one and doesn't add delimeter after
        for y in self.qtys:
            if self.qtys.index(y) == len(self.qtys) - 1:
                cartfile.write(y + ", ")
            else:
                cartfile.write(y + ":")

        cartfile.close()
