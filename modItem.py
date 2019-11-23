#modItem.py

def main():
    print(__file__.split('/')[-1])
def readandwrite():
    a=open("check.txt","r")
    b=a.readlines()
    a.close()
    c=int(input("Which number do you want to modify?"))
    d=c-1
    b[d]=input("Whant content do you want to update?")
    b[d]=b[d]+"\n"
    print(b)
    index=0
    e=open("check.txt","w")
    while index<29:
        e.write(b[index])
        index=index+1
    e.close()
readandwrite()

        
