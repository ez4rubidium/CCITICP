#delItem.py
import os

def find(rNum):
    with open("inventory.txt", "r") as inF:
        data_list = inF.readlines()
        inF.close()
    serLine = str(rNum) + "\n"
    try:
        tLine = data_list.index(serLine)
    except ValueError as err:
            #print(err)
            print("Item Not Found")
            tLine = None
    return tLine

def writeChanges(data_list):
    
    comfor = 0
    iChar = input("Enter 'yes' to delete the item: ")
    if iChar == "yes":
        with open("inventory.txt", "w") as oF:
            oF.writelines(data_list)
            oF.close()
    else:
        print("No changes made!")

def del_Line(tLine):
    with open("inventory.txt", "r") as inF:
        data_list = inF.readlines()
        inF.close()
    #bakup to temp
    with open("temp.txt", "w") as temp:
        temp.writelines(data_list)
        temp.close()
    try:
        del_list = data_list[tLine : tLine + 10]
        del data_list[tLine : tLine + 10]
        print("-"*60)
        print(del_list)
        print("-"*60)
        print("This is the item you are going to delete")
        with open("del_list.txt", "w") as dFile:
            dFile.writelines(del_list)
            dFile.close()
        writeChanges(data_list)
    except TypeError as err:
        #print(err)
        print("No changes made")
    


def main():
    print(__file__.split('/')[-1])

    repeat = 1
    while repeat == 1:
        rNum = input("Enter a Record Number: ")
        tLine = find(rNum)
        del_Line(tLine)
        ask =1 
        while ask == 1:
            inChar = input("Do you want delete another itam record? (y/n): ")
            if inChar == "n":
                os.remove("temp.txt")
                ask = 0
                repeat = 0
            elif inChar == "y":
                ask = 0


if __name__ == '__main__':
    main()
    
