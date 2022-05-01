import os


class Inventory:

    def __init__(self):
        self.isbns = []
        self.qty = []
        
        ## Finds file path 
        here = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(here, 'inventory.txt')
        
        # Opens files
        try:
            f = open("Inventory.txt", "r")
            f_contents = f.read()
            lines = f_contents.splitlines()
                
            for x in lines:        
             isbn_content = x.split(',')
             self.isbns.append(isbn_content)
             qty_content = int(x)
             self.qty.append(qty_content)
            f.close()
        
        except IOError:
            print("File not found")
            return "-1"


    def getqty(self):
        return self.isbns

    def edit_qty(self, isbn, qty):
        i = 0
        while i < len(self.isbns):
            if self.isbns[i] == isbn:
                self.qtys[i] = int(self.qtys[i]) - int(qty)
                break
            else:
                i += i

    def create_new_file(self, isbn, title, author, genre, qty, price):
        here = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(here, 'inventory.txt')
        f = open(filename, "New Inventory")
        f.write(isbn + "," + title + ", " + author + ", " + genre + ", " + qty + ", " + price)
        f.close





