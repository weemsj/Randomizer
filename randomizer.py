import http.server
import random
import time

hostName = "localhost"
serverPort = 8080

def randomizer():
    
    while True:
        time.sleep(3)
        f = open('pipeline.txt', 'r')

        contents = f.readline()

        # checks for a single number
        if contents.isdigit():
            num = int(contents)
            rand = random.randrange(num)

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
        
                if len(lis) == 3:
                    rand = random.randrange(lis[0], lis[1], lis[2])
                elif len(lis) == 2:
                    rand = random.randrange(lis[0], lis[1])
                else:
                    rand = random.randrange(lis[0])

            else:
                num = len(lis)
                if num <= 1:
                    return 
                randNum = random.randrange(num)
                rand = lis[randNum]

        with open('pipeline.txt', 'w') as f:
                f.write(rand)
    
            

if __name__ == "__main__":
   randomizer()
