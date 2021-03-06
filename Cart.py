class Cart:
    
    def __init__(self, Customer_id):
        self.Customer_id = Customer_id
        
        self.Cart_id = 1
        cartfile = open("carts.txt", "r")
        # initilizes cart id variable at 1 and adds one for every existing cart id, makes new cart_id one more than current number
        for line in cartfile:
            self.Cart_id += self.Cart_id
            
        self.ISBNs = []
        self.qtys = []
    
    def addItem(self, ISBN, qty):
        # checks to see if ISBN already exists in cart. If it does, simply adds the given qty to current
        for x in self.ISBNs:
            if x == ISBN:
                self.qtys[self.ISBNs.index(x)] = self.qtys[self.ISBNs.index(x)] + qty
                return True
        self.ISBNs.append(ISBN)
        self.qtys.append(qty)
        
    def remItem(self, ISBN, qty):
        for x in self.ISBNs:
            if x == ISBN: 
                if qty < self.qtys[self.ISBNs.index(x)]:
                    self.qtys[self.ISBNs.index(x)] = self.qtys[self.ISBNs.index(x)] - qty
                    return True
                elif qty == self.qtys[self.ISBNs.index(x)]:
                    del self.qtys[self.ISBNs.index(x)]
                    del self.ISBNs[self.ISBNs.index(x)]
                    return True
                else:
                    return False
        return False
    
    def getCSTid(self):
        return self.Customer_id
    
    def getISBNs(self):
        return self.ISBNs()
    
    def getQTYs(self):
        return self.qtys()
    
    def commitToFile(self):
        # opens file
        cartfile = open("cars.txt", "a")
        # writes cart_id and customer_id 
        cartfile.write(self.Cart_id, ", ", self.Customer_id, ", ",)
        
        # loops through isbn list and writes them to file and doesn't add delimeter after
        for x in self.ISBNs:
            if self.ISBNs.index(x) == len(self.ISBNs) - 1:
                cartfile.write(x, ", ")
            cartfile.write(x, ":")
            
        # loops through qtys list and writes them to file, accounts for the last one and doesn't add delimeter after
        for y in self.qtys:
            if self.qtys.index(y) == len(self.qtys) - 1:
                cartfile.write(y, ", ")
            else:
                cartfile.write(y, ":")
                
        cartfile.close()