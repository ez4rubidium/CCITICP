#main 
import test
import addItem
import dispItem
import searItem
import modItem
import delItem

def menu(i):
    switch = {
        0 : test.main,
        1 : addItem.main,
        2 : dispItem.main,
        3 : searItem.main,
        4 : modItem.main,
        5 : delItem.main,
        6 : quit
        }
    switch[i]()

def main():
    x = 1
    while x == 1: 
        inputChar=""
        print("""
        1. Add New Item(s): 
        2. Display Item Record(s): 
        3. Search Item Infomation: 
        4. Modify Item Record(s): 
        5. Delete Item Record(s): 
        """)

        inputChar = input("Please select a item by enter a char: ")
        x = 0
        try:
            val = int(inputChar)
            
        except ValueError as err:
            x = 1
            print(err)
    
    print(val)
    menu(val) 

main()
