from typing_extensions import Self


class Inventory:

    def __init__(title, inventory_id):
        Self.title = title
        
        Self.inventory_id = inventory_id
        try:
             f = open("Inventory.txt", "r") as file:
             for item in file:
                print(item)
                content = item.split(',')
                if content[0] == inventory_id:
                    return content[1]
                return "-1"
        except IOError:
            print("File not found")
            return "-1"


    def getqty(ISBN, qty):
        lines = []
        with open(r"Inventory.txt", 'r') as fp:
            lines = fp.readlines()

    #write file
    with open(r"Inventory.txt" 'w') as fp:
        for number, line in enumerate(lines):
            


## This will open the inventory text file and read all its content. 

   # f = open("inventory.txt", "r+")

    #d = f.readlines()
    #f.seek(0)

    #for i in d:
     #   if i != "line you want to remove: ":
      #      f.write(i)
    #f.truncate()



