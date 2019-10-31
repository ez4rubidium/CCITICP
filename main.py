#main 
import test
import addItem
import dispItem
import searItem
import modItem
import delItem


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
    if inputChar == test.testChar:
        print(test.testFunc(5))

main()
