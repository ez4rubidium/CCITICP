#main 
#import test
#import addItem
#import dispItem
#import searItem
#import modItem
#import delItem

def menu(i):
    switch={
        "0": "test",
        "1": "addItem",
        "2": "DispItem",
        "3": "SearItem",
        "4": "ModItem",
        "5": "DelItem"
        }
    return switch.get(i, "Invalid Input")

def main():
    inputChar=""
    print("""
    1. Add New Item(s): 
    2. Display Item Record(s): 
    3. Search Item Infomation: 
    4. Modify Item Record(s): 
    5. Delete Item Record(s): 
    """)

    inputChar = input("Please select a item by enter a char: ")
    print(menu(inputChar))

main()
