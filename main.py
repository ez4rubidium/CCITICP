#main 
import test
import addItem
import dispItem
import searItem
import modItem
import delItem

def quit():
    q = 1
    print("Have a nice day!! Goodbye.")
    exit()

def menu(i):
    switch = {
        "0" : test.main,
        "1" : addItem.main,
        "2" : dispItem.main,
        "3" : searItem.main,
        "4" : modItem.main,
        "5" : delItem.main,
        "q" : quit
        }
    switch[i]()

def main():
    q = 0
    x = 1
    while x == 1: 
        inputChar=""
        while q == 0:
            print("""
        1. Add New Item(s): 
        2. Display Item Record(s): 
        3. Search Item Infomation: 
        4. Modify Item Record(s): 
        5. Delete Item Record(s): 
        q. Quit the program: 
            """)
            inputChar = input("Please select a item by enter a char: ")
            
            try:
                x = 0
                menu(inputChar)
                input("Press [Enter] to continue...")
            except KeyError as err:
                x = 1
                print("Invaild Input ", err)


main()
