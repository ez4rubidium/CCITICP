#dispItem.py

def main():
    print(__file__.split('/')[-1])
    fileName = input("Enter an INPUT file name for reading:")
    readdata(fileName)

def readdata(file_name):
    inFile = open(file_name, "r")
    recNum = str(inFile.readline())

    while recNum != "":
        itemName = str(inFile.readline())
        itemNum = str(inFile.readline())
        category = str(inFile.readline())
        quantity = str(inFile.readline())
        weight = str(inFile.readline())
        recipient = str(inFile.readline())
        finalDes = str(inFile.readline())
        delStatus = str(inFile.readline())
        blankLine = inFile.readline()

        print("Record Number:", recNum, end="")
        print("Item Name:", itemName, end="")
        print("Item Number:", itemNum, end="")
        print("Category:", category, end="")
        print("Quanity:", quantity, end="")
        print("Weight:", weight, end="")
        print("Recipient:", recipient, end="")
        print("Final Destination:", finalDes, end="")
        print("Delivery Status: ", delStatus, sep="")

        recNum = str(inFile.readline())
        
    inFile.close()

main()
