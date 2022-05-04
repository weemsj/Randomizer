import time


def write(lis):
    with open('pipeline.txt', 'w') as f:
        for i in lis: 
            if i != lis[-1]:  # if the list item is the only item or is the last item dont include a comma at the end.
                if type(i) == int: # check for an integer write function only works with strings.
                    i = str(i)
                f.write(i + ",")
            else:
                if type(i) == int:
                    i = str(i)
                f.write(i)
    f.close()


def read():
    f = open('pipeline.txt', 'r')
    contents = f.readline()
    f.close()
    print(contents)
    

if __name__ == '__main__':
    
    """ Below are some example calls of what data the randomizer expects to read from the pipeline.txt file."""
    write([15]) # user passes a single int (stop)
    time.sleep(3.5)
    read()
    lis = []    # clears the pipeline.txt file
    write(lis)
    
    write([10,30]) # user passes two ints (start, stop)
    time.sleep(3.5)
    read()
    lis = []
    write(lis)
    
    write([10,30, 2]) # user passes three ints (start, stop, step)
    time.sleep(3.5)
    read()
    lis = []
    write(lis)
    
    write(['little']) # user one string
    time.sleep(3.5)
    read()
    lis = []
    write(lis)
    
    write(['small', 'big', 'medium', 'large', 'gigantic']) # user passes multiple strings
    time.sleep(3.5)
    read()
    lis = []
    write(lis)
    
    write(['10 Smallest Pigeons', 'The Top 50 Most Dangerous Animals', '100 Shocking Facts' ]) # user passes strings that contain numbers
    time.sleep(3.5)
    read()
    lis = []
    write(lis)
    
    write(['']) # if user passes emplty string no crashes occur but also no errors are returned
    time.sleep(3.5)
    read()
    lis = []
    write(lis)
    
    write([30,10]) # if user passes a larger start than stop, the randomizer will return an error message
    time.sleep(3.5)
    read()
    lis = []
    write(lis)
    
    