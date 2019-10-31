#main 
import test
import addItem
import dispItem
import searItem
import modItem
import delItem


def main():
    inputChar=""
    print("""
    something 1
    item 2
    crap 3
    """)

    inputChar = input("Please select a item by enter a char: ")
    if inputChar == test.testChar:
        print(test.testFunc(5))

main()
