#test.py
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
    switch={
        "0": "test",
        "1": "addItem",
        "2": "DispItem",
        "3": "SearItem",
        "4": "ModItem",
        "5": "DelItem"
        }
    return switch.get(i, "Invalid Input")
print(menu("1"))