import os


class Book:
    def __init__(self, isbn):
        self.isbn = isbn
        self.title = ""
        self.author = ""
        self.genre = ""
        self.amount = ""
        self.price = ""

        # Finds files in directory
        here = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(here, 'inventory.txt')

        # Opens files
        f = open(filename, "r")
        file_contents = f.read()
        lines = file_contents.splitlines()

        for x in lines:
            linelist = x.split(", ")
            if linelist[0] == self.isbn:
                self.title = linelist[1]
                self.author = linelist[2]
                self.genre = linelist[3]
                self.amount = linelist[4]
                self.price = linelist[5]
                break
        f.close()

    def get_isbn(self):
        return self.isbn

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_genre(self):
        return self.genre

    def get_amount(self):
        return self.amount

    def get_price(self):
        return self.price

    def reduce_amount(self, qty):
        if qty <= int(self.amount):
            self.amount = str(int(self.amount) - qty)
            return True
        if qty > int(self.amount):
            return False

    def increase_amount(self, qty):
        self.amount = self.amount + qty
