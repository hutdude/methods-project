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
            if x.split(", ") == self.isbn:
                self.title = x.split(", ")
                self.author = x.split(", ")
                self.genre = x.split(", ")
                self.amount = x.split(", ")
                self.price = x
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
        if qty <= self.amount:
            self.amount = self.amount - qty
            return True
        if qty > self.amount:
            return False

    def increase_amount(self, qty):
        self.amount = self.amount + qty

    def commit_to_file(self):
