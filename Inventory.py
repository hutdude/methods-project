import os


class Inventory:
    def __init__(self):
        self.isbns = []
        self.qtys = []

        # Finds files in directory
        here = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(here, 'inventory.txt')

        # Opens files
        f = open(filename, "r")
        file_contents = f.read()
        lines = file_contents.splitlines()

        for x in lines:
            temp_isbn = x.split(", ")
            self.isbns.append(temp_isbn)
            temp_null = x.split(", ")
            temp_null2 = x.split(", ")
            temp_null3 = x.split(", ")
            temp_qty = int(x)
            self.qtys.append(temp_qty)
        f.close()

    def get_isbns(self):
        return self.isbns

    def sub_qty(self, isbn, qty):
        i = 0
        while i < len(self.isbns):
            if self.isbns[i] == isbn:
                self.qtys[i] = int(self.qtys[i]) - int(qty)
                break
            else:
                i += i

    def add_qty(self, isbn, qty):
        i = 0
        while i < len(self.isbns):
            if self.isbns[i] == isbn:
                self.qtys[i] = int(self.qtys[i]) + int(qty)
                break
            else:
                i += i

    def commit_book_to_file(self, isbn, title, author, genre, qty, price):
        here = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(here, 'inventory.txt')
        f = open(filename, "a")
        f.write(isbn + ", " + title + ", " + author + ", " + genre + ", " + qty + ", " + price)
        f.close()