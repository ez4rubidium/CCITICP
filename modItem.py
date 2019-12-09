#modItem.py

def main1():
    print(__file__.split('/')[-1])
def main():
    main1()
    a=int(input("What record number do you want to update?"))
    read(a)
    readandwrite(a)
    j=input("Do you want to continue modify? (y/n)")
    if j=="y":
        main()
def read(a):
    a=a-1001
    b=open("inventory.txt","r")
    c=a*10
    for d in range(c):
         e=b.readline()
    f=b.readline()
    g=b.readline()
    h=b.readline()
    i=b.readline()
    j=b.readline()
    k=b.readline()
    l=b.readline()
    n=b.readline()
    m=b.readline()
    b.close()
    print("Record number:",f,end="")
    print("Item name:",g,end="")
    print("Item number:",h,end="")
    print("Category:",i,end="")
    print("Quantity:",j,end="")
    print("Weight:",k,end="")
    print("Recipient:",l,end="")
    print("Final Destination:",n,end="")
    print("Delivery status:",m,end="")
def readandwrite(a):
    z=a-1001
    x=z*10
    o=input("What items in this record you want to change?")
    if o=="Record number":
        b=open("inventory.txt","r")
        c=b.readlines()
        b.close()
        c[x]=input("What information you want to update?")
        c[x]=c[x]+"\n"
        index=0
        count=0
        for n in c:
            count=count+1
        e=open("inventory.txt","w")
        while index<count:
            e.write(c[index])
            index=index+1
        e.close()
    elif o=="Item name":
        b=open("inventory.txt","r")
        c=b.readlines()
        b.close()
        x=x+1
        c[x]=input("What information you want to update?")
        c[x]=c[x]+"\n"
        index=0
        count=0
        for n in c:
            count=count+1
        e=open("inventory.txt","w")
        while index<count:
            e.write(c[index])
            index=index+1
        e.close()
    elif o=="Item number":
        b=open("inventory.txt","r")
        c=b.readlines()
        b.close()
        x=x+2
        c[x]=input("What information you want to update?")
        c[x]=c[x]+"\n"
        index=0
        count=0
        for n in c:
            count=count+1
        e=open("inventory.txt","w")
        while index<count:
            e.write(c[index])
            index=index+1
        e.close()
    elif o=="Category":
        b=open("inventory.txt","r")
        c=b.readlines()
        b.close()
        x=x+3
        c[x]=input("What information you want to update?")
        c[x]=c[x]+"\n"
        index=0
        count=0
        for n in c:
            count=count+1
        e=open("inventory.txt","w")
        while index<count:
            e.write(c[index])
            index=index+1
        e.close()
    elif o=="Quantity":
        b=open("inventory.txt","r")
        c=b.readlines()
        b.close()
        x=x+4
        c[x]=input("What information you want to update?")
        c[x]=c[x]+"\n"
        index=0
        count=0
        for n in c:
            count=count+1
        e=open("inventory.txt","w")
        while index<count:
            e.write(c[index])
            index=index+1
        e.close()
    elif o=="Weight":
        b=open("inventory.txt","r")
        c=b.readlines()
        b.close
        x=x+5
        c[x]=input("What information you want to update?")
        c[x]=c[x]+"\n"
        index=0
        count=0
        for n in c:
            count=count+1
        e=open("inventory.txt","w")
        while index<count:
            e.write(c[index])
            index=index+1
        e.close()
    elif o=="Recipient":
        b=open("inventory.txt","r")
        c=b.readlines()
        b.close()
        x=x+6
        c[x]=input("What information you want to update?")
        c[x]=c[x]+"\n"
        index=0
        count=0
        for n in c:
            count=count+1
        e=open("inventory.txt","w")
        while index<count:
            e.write(c[index])
            index=index+1
        e.close()
    elif o=="Final Destination":
        b=open("inventory.txt","r")
        c=b.readlines()
        b.close()
        x=x+7
        c[x]=input("What information you want to update?")
        c[x]=c[x]+"\n"
        index=0
        count=0
        for n in c:
            count=count+1
        e=open("inventory.txt","w")
        while index<count:
            e.write(c[index])
            index=index+1
        e.close()
    elif o=="Delivery status":
        b=open("inventory.txt","r")
        c=b.readlines()
        b.close()
        x=x+8
        c[x]=input("What information you want to update?")
        c[x]=c[x]+"\n"
        index=0
        count=0
        for n in c:
            count=count+1
        e=open("inventory.txt","w")
        while index<count:
            e.write(c[index])
            index=index+1
        e.close()
    else:
        print("error")
if __name__ == '__main__':
    main()
    
#finish
 