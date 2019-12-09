#test.py
from random import randint
from time import sleep

def main():
    target_phrase = 'Hello, World!'
    build_phrase = ''
    i = 0
    while i < len(target_phrase): 
        guess_letter = chr(randint(32, 126))   
        print(build_phrase + guess_letter)
        if guess_letter == target_phrase[i]:
            build_phrase += guess_letter
            i += 1    
        sleep(.002)
if __name__ == '__main__':
    main()
            
print("Hello world!")
# read the data file in as a list
#with open("test.txt", "r") as inF:
#    data_list = inF.readlines()
#    inF.close()
# test it ...
#print(data_list)
 
#print('-'*60)

#t = 9
# remove list items from index 3 to 5 (inclusive)
#del data_list[t:t+9]
# test it ...
#print(data_list)
 
## write the changed data (list) to a file
#fout = open("MyData2.txt", "w")
#fout.writelines(data_list)
#fout.close()
