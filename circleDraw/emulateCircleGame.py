



def emulateGame(numPeople, jmpSize = 1): 

    
    listOfPeople = list(range(numPeople))
    currPersonIndex = 0 
    
    while len(listOfPeople) > 1:
        del listOfPeople[(currPersonIndex + jmpSize) % len(listOfPeople)]
        currPersonIndex = (currPersonIndex + 1) % (len(listOfPeople) + 1) 



    return str(numPeople) + ': ' + str(listOfPeople[0] + 1) 
    

for i in range(100):
    print(emulateGame(i + 1, 2))