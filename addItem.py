#addItem.py

def main():
    print(__file__.split('/')[-1])
    fileName = input("Enter a OUTPUT file name for writing:")
    writedata(fileName)

def writedata(file_name):
    outFile = open(file_name, "w")

    for itemRecord in range(1,51):
        print("Item Record #", itemRecord, sep=" ")
        recNum = str(input("Please enter Record Number:"))
        itemName = str(input("Please enter Item Name:"))
        itemNum = str(input("Please enter Item Number:"))
        category = str(input("Please enter Category:"))
        quantity = str(input("Please enter Quantity:"))
        weight = str(input("Please enter Weight:"))
        recipient = str(input("Please enter Recipient:"))
        finalDes = str(input("Please enter Final Destination:"))
        delStatus = str(input("Please enter Delivery Status:"))
    
        outFile.write(recNum + "\n")
        outFile.write(itemName + "\n")
        outFile.write(itemNum + "\n")
        outFile.write(category + "\n")
        outFile.write(quantity + "\n")
        outFile.write(weight + "\n")
        outFile.write(recipient + "\n")
        outFile.write(finalDes + "\n")
        outFile.write(delStatus + "\n\n")

        addItem = input("\nDo you want to add another item record? (y/n):")
        if addItem == "n":
            break
        
    outFile.close()

#main()
