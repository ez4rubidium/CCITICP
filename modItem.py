#modItem.py

def main():
    print(__file__.split('/')[-1])
g=int(input("What record number do you want to update?"))
g=g-1001
a=open("check.txt","r")
n=g*10
for h in range(n):
        e=a.readline()
i=input("What items in this record you want to change?")
bb=input("What new information would you set ?")
if i=="record number":
    aa=a.readline()
    aa=bb
    c=a.read()
    a.close()
    b=open("check.txt","w")
    y=b.write(bb)
    yy=b.write("\n")
    oo=b.write(c)
    b.close()
elif i=="Item name":
    for nn in range(1):
        cc=a.readline()
    dd=a.readline()
    dd=bb
    c=a.read()
    a.close()
    b=open("check.txt","w")
    y=b.write(cc)
    oo=b.write(dd)
    yy=b.write("\n")
    zz=b.write(c)
    b.close()
else:
    print(aaa)
   #have not finish

        
