import os

class book():
    def __init__(self, isbn, title, author, genre, amount):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre
        self.amount = amount

    #Creates Lists for the lines and split contents
    lines = []
    comma = []
        
    #Finds files in directory
    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, 'inventory.txt')

    #Opens files 
    f = open(filename, "r")
    filecontents = f.read()
    splitcontents = filecontents.splitlines()

    lines = splitcontents

    #Splits strings in file by comma
    comma = lines[0].split(', ')
    print(comma)

    #While loop for finding and replacing < >
    i = 0 
    while i < len(comma):
        comma[i] = comma[i].replace("<", "")
        comma[i] = comma[i].replace(">", "")
        i = i + 1

    #Store list objects in variables
    isbn = comma[0], comma[5]
    title = comma[1], comma[6]
    author = comma[2], comma[7]
    genre = comma[3], comma[8]
    amount = comma[4], comma[9]

    print(isbn)
    print(title)
    print(author)
    print(genre)
    print(amount)

    f.close()


