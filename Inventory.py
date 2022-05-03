import os


class Inventory:

    def __init__(self):
        self.isbns = []
        self.qty = []

        # Finds file path
        here = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(here, 'inventory.txt')

        # Opens files
        try:
            f = open("Inventory.txt", "r")
            f_contents = f.read()
            lines = f_contents.splitlines()

            for x in lines:
                isbn_content_raw = x.split(", ")
                self.isbns.append(isbn_content_raw[0])
                qty_content = int(isbn_content_raw[4])
                self.qty.append(qty_content)
            f.close()

        except IOError:
            print("File not found")

    def get_isbns(self):
        return self.isbns

    def get_qtys(self):
        return self.qty

    def edit_qty(self, isbn, qty):
        i = 0
        while i < len(self.isbns):
            if self.isbns[i] == isbn:
                self.qty[i] = int(self.qty[i]) - int(qty)
                break
            else:
                i += 1

    def commit_book_to_file(self, isbn, title, author, genre, qty, price):
        here = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(here, 'inventory.txt')
        f = open(filename, "a")
        f.write(isbn + ", " + title + ", " + author + ", " + genre + ", " + qty + ", " + price + "\n")
        f.close()
