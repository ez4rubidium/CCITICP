#modItem.py
def main1():
    print(__file__.split('/')[-1])
def main():
    main1()
    recNum=int(input("What record number do you want to update?"))
    read(recNum)
    readandwrite(recNum)
    modcontinue=input("Do you want to continue modify? (y/n)")
    if modcontinue=="y":
        main()
def read(recNum):
    recNum=recNum-1001
    openfile=open("inventory.txt","r")
    lines=recNum*10
    for number in range(lines):
         readthings=openfile.readline()
    recNum1=openfile.readline()
    ItemName1=openfile.readline()
    ItemNumber1=openfile.readline()
    Category1=openfile.readline()
    Quantity1=openfile.readline()
    Weight1=openfile.readline()
    Recipient1=openfile.readline()
    FinDest1=openfile.readline()
    DeliveryStat1=openfile.readline()
    openfile.close()
    print("Record number:",recNum1,end="")
    print("Item name:",ItemName1,end="")
    print("Item number:",ItemNumber1,end="")
    print("Category:",Category1,end="")
    print("Quantity:",Quantity1,end="")
    print("Weight:",Weight1,end="")
    print("Recipient:",Recipient1,end="")
    print("Final Destination:",FinDest1,end="")
    print("Delivery status:",DeliveryStat1,end="")
def readandwrite(recNum):
    calrecNum=recNum-1001
    countline1=calrecNum*10
    inPutrecNum=input("What items in this record you want to change?")
    if inPutrecNum=="Record number":
        openfile=open("inventory.txt","r")
        lines=openfile.readlines()
        openfile.close()
        lines[countline1]=input("What information you want to update?")
        lines[countline1]=lines[countline1]+"\n"
        index=0
        count=0
        for n in lines:
            count=count+1
        readthings=open("inventory.txt","w")
        while index<count:
            readthings.write(lines[index])
            index=index+1
        readthings.close()
    elif inPutrecNum=="Item name":
        openfile=open("inventory.txt","r")
        lines=openfile.readlines()
        openfile.close()
        countline1=countline1+1
        lines[countline1]=input("What information you want to update?")
        lines[countline1]=lines[countline1]+"\n"
        index=0
        count=0
        for n in lines:
            count=count+1
        readthings=open("inventory.txt","w")
        while index<count:
            readthings.write(lines[index])
            index=index+1
        readthings.close()
    elif inPutrecNum=="Item number":
        openfile=open("inventory.txt","r")
        lines=openfile.readlines()
        openfile.close()
        countline1=countline1+2
        lines[countline1]=input("What information you want to update?")
        lines[countline1]=lines[countline1]+"\n"
        index=0
        count=0
        for n in lines:
            count=count+1
        readthings=open("inventory.txt","w")
        while index<count:
            readthings.write(lines[index])
            index=index+1
        readthings.close()
    elif inPutrecNum=="Category":
        openfile=open("inventory.txt","r")
        lines=openfile.readlines()
        openfile.close()
        countline1=countline1+3
        lines[countline1]=input("What information you want to update?")
        lines[countline1]=lines[countline1]+"\n"
        index=0
        count=0
        for n in lines:
            count=count+1
        readthings=open("inventory.txt","w")
        while index<count:
            readthings.write(lines[index])
            index=index+1
        readthings.close()
    elif inPutrecNum=="Quantity":
        openfile=open("inventory.txt","r")
        lines=openfile.readlines()
        openfile.close()
        countline1=countline1+4
        lines[countline1]=input("What information you want to update?")
        lines[countline1]=lines[countline1]+"\n"
        index=0
        count=0
        for n in lines:
            count=count+1
        readthings=open("inventory.txt","w")
        while index<count:
            readthings.write(lines[index])
            index=index+1
        readthings.close()
    elif inPutrecNum=="Weight":
        openfile=open("inventory.txt","r")
        lines=openfile.readlines()
        openfile.close
        countline1=countline1+5
        lines[countline1]=input("What information you want to update?")
        lines[countline1]=lines[countline1]+"\n"
        index=0
        count=0
        for n in lines:
            count=count+1
        readthings=open("inventory.txt","w")
        while index<count:
            readthings.write(lines[index])
            index=index+1
        readthings.close()
    elif inPutrecNum=="Recipient":
        openfile=open("inventory.txt","r")
        lines=openfile.readlines()
        openfile.close()
        countline1=countline1+6
        lines[countline1]=input("What information you want to update?")
        lines[countline1]=lines[countline1]+"\n"
        index=0
        count=0
        for n in lines:
            count=count+1
        readthings=open("inventory.txt","w")
        while index<count:
            readthings.write(lines[index])
            index=index+1
        readthings.close()
    elif inPutrecNum=="Final Destination":
        openfile=open("inventory.txt","r")
        lines=openfile.readlines()
        openfile.close()
        countline1=countline1+7
        lines[countline1]=input("What information you want to update?")
        lines[countline1]=lines[countline1]+"\n"
        index=0
        count=0
        for n in lines:
            count=count+1
        readthings=open("inventory.txt","w")
        while index<count:
            readthings.write(lines[index])
            index=index+1
        readthings.close()
    elif inPutrecNum=="Delivery status":
        openfile=open("inventory.txt","r")
        lines=openfile.readlines()
        openfile.close()
        countline1=countline1+8
        lines[countline1]=input("What information you want to update?")
        lines[countline1]=lines[countline1]+"\n"
        index=0
        count=0
        for n in lines:
            count=count+1
        readthings=open("inventory.txt","w")
        while index<count:
            readthings.write(lines[index])
            index=index+1
        readthings.close()
    else:
        print("error")
if __name__ == '__main__':
    main()

    

#finish

 
            

        


    
