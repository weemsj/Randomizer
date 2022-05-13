
import random
import time


def randomizer():
    
    time.sleep(3)
    
    '''
    alternative content options for other uses. 
    
    For CS361 microservis created for nathan we will only find random values from zero to 100. 
    
    For other use cases outside of CS361 portfolio project, uncomment f= and content = , for futher information on how to use this program see ReadMe
    
    f = open('pipeline.txt', 'r')

    contents = f.read()
    
    '''
    
    contents = "100"

    if not contents:
        return 
    
    # checks for a single number
    if contents.isdigit():
        num = int(contents)
        rand = random.randrange(num)
        time.sleep(1.5)
        
    else:
        isNum = 0
        # puts contents into a list of strings
        lis = contents.split(',')

        # checks for a list of 3 strings or less indicating a possible string of numbers
        # if len(lis) <=3 then check each if each string is a number, if all string are numbers randomize by range.
        if len(lis) <= 3:
            for i in lis:
                if i.isdigit():
                    isNum = True
                else:
                    isNum = False

        if isNum == True:  # indicates a list of numbers
            for i in range(len(lis)):
                lis[i] = int(lis[i])
        
            if len(lis) == 3 and lis[0] < lis[1] > lis[2]:
                rand = random.randrange(lis[0], lis[1], lis[2])
            elif len(lis) == 2 and lis[0]< lis[1]:
                rand = random.randrange(lis[0], lis[1])
            elif len(lis) == 1:
                rand = random.randrange(lis[0])
            else:
                with open('pipeline.txt', 'w') as f:
                    f.write("Error, invalid integer, randomizer expects (start,stop,step) start value should be less than stop, and step value should be less than stop . Start and step are optional. ")
                    f.close()
                    return
        else:
            num = len(lis)
            if num <= 1:
                return 
            randNum = random.randrange(num)
            rand = lis[randNum]

    with open('pipeline.txt', 'w') as f:
        if type(rand) == int:
            rand = str(rand)
        f.write(rand)
        f.close()
        return
        
    
            

if __name__ == "__main__":
   while True:
        randomizer()
