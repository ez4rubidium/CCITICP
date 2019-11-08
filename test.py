#test.py
import addItem
import dispItem
import searItem
import modItem
import delItem

testValue = 25
testString = "This is a test."
testChar = "F"
testList = [2, 4, 6, 8, 10]

def testFunc(i):
    total = i + i ** 10
    return total

def testfunc2(j):
    total = j ** j
    return total

def menu(i):
    switch = {
        "0" : addItem.main,
        "1" : addItem.main,
        "2" : dispItem.main,
        "3" : searItem.main,
        "e" : modItem.main,
        "q" : delItem.main
        }
    try:
        switch[i]()
    except KeyError as err:
        print(err)


def main():
    menu(input("Input : "))
    pass

#main()
