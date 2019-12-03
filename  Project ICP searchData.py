#searchData.py
import os.path

def main():
    print(__file__.split('/')[-1])
    fileName = input("Enter a OUTPUT file name for writing:")
    searchData(fileName)

def searchData(fileName):
    recNum = int(input("Please enter Record Number:"))

    inFile = open(fileName, "r")
    print()

    itemName = str(inFile.readline())
    itemNum = int(inFile.readline())
    category = inFile.readline()
    quantity = int(inFile.readline())
    weight = int(inFile.readline())
    recipient = inFile.readline()
    finalDes = inFile.readline()
    delStatus = inFile.readline()

    print("Item Name:", itemName, end="")
    print("Item Number:", itemNum, end="")
    print("Category:", category, end="")
    print("Quantity:", quantity, end="")
    print("Weight:", weight, end="")
    print("Recipient:", recipient, end="")
    print("Final Destination:", finalDes, end="")
    print("Delivery Status:", delStatus)
    print()

    recNum = inFile.readline()
    inFile.close()

    searchData()

main()

    

    
    
    
    
    
   

    
        
    
