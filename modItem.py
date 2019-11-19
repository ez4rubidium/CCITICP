#modItem.py

def main():
    print(__file__.split('/')[-1])
def main1():
    number=int(input("What record do you want to update?"))
    step1(number)
def step1(number):
    a=open("inventory.txt","r")
    b=a.readlines()
    if b==number:
        data=input("What item do you want to change?")
        if data=="Record number":
            
        
