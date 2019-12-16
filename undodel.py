#undodel.py
import os

def find(rNum):
    with open("inventory.txt", "r") as inF:
        data_list = inF.readlines()
        inF.close()
    serLine = str(rNum) + "\n"
    try:
        tLine = int(data_list.index(serLine))
    except ValueError as err:
            tLine = -1 
    return tLine

def writeChanges(data_list):
    comfor = 0
    iChar = input("Enter 'yes' to restore the item: ")
    if iChar == "yes":
        with open("inventory.txt", "w") as oF:
            oF.writelines(data_list)
            oF.close()
        print("Item restored!")
        with open("del_list.txt", "w") as dF:
            dF.writelines("")
            dF.close()
    else:
        print("No changes made!")

def ins_Line(tLine, ins_list):
    with open("inventory.txt", "r") as inF:
        data_list = inF.readlines()
        inF.close()
    #bakup to temp
    with open("temp.txt", "w") as temp:
        temp.writelines(data_list)
        temp.close()
    try:
        if tLine == -1:
            ins_list = "".join(ins_list)
            data_list.append(ins_list)
        else:
            ins_list = "".join(ins_list)
            data_list.insert(tLine, ins_list)
        print("A preview of the restored data")
        print("-"*80)
        print(data_list)
        print("-"*80)
        writeChanges(data_list)
    except TypeError as err:
        #print(err)
        print("No changes made")
    
def main():
    try:
        with open("del_list.txt", "r") as dFile:
            del_list = dFile.readlines()
            dFile.close()
        rNum = int(del_list[0][0:-1]) + 1
        disN =["Record number", "Item name", "Item number", "Category", "Quantity", "Weight", "Recipient", "Final destination", "Delivery status"]
        print("This is the previous deleted record: \n")
        for i in range(len(disN)):
            print(disN[i], ":", del_list[i],end = "")
    except UnboundLocalError and IndexError as err:
        rNum = None
        #print(err)
        print("No previously deleted record")
    input("\nPress [Enter] to continue")
    if rNum != None:
        tLine =find(rNum)
        ins_Line(tLine, del_list)
    else:
        print()
    print("Handle data with care.")
    os.remove("temp.txt")

if __name__ == '__main__':
    main()