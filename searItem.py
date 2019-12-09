#searItem.py
import os

def main():
    print(__file__.split('/')[-1])

    while(True):
        itemRec_input = int(input("\nPlease enter Record Number for Advanced Searching:"))
        itemRec_input = itemRec_input-1001
        inFile = open("inventory.txt", "r")
        index = itemRec_input*10
        for itemRec in range(index) :
            e = inFile.readline()
        recNum1 = inFile.readline()
        itemName1 = inFile.readline()
        itemNum1 = inFile.readline()
        category1 = inFile.readline()
        quantity1 = inFile.readline()
        weight1 = inFile.readline()
        recipient1 = inFile.readline()
        finalDes1 = inFile.readline()
        delStatus1 = inFile.readline()
        inFile.close()

        print("Record Number:", recNum1, end="") 
        print("Item Name:", itemName1, end="")
        print("Item Number:", itemNum1, end="")
        print("Category:", category1, end="")
        print("Quantity:", quantity1, end="")
        print("Weight:", weight1, end="")
        print("Recipient:", recipient1, end="")
        print("Final Destination:", finalDes1, end="")
        print("Delivery Status:", delStatus1, end="")

        searchItem = input("Do you want to search another item record? (y/n):")
        if searchItem == "n":
            print("\nHope to see you next time ^.^")
            break
if __name__ == '__main__':
    main()
    