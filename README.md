# Randomizer
 A micro-service that reads a value in a text file if the value is a string array or range of numbers it clears the contents of the text file and writes a random value from the array or range. 

# here is a sample function call order

write(['small', 'big', 'medium', 'large', 'gigantic']) # user passes multiple strings
time.sleep(3.5)
read()
lis = []
write(lis)


# how user should pass a list to the text file

lis = ["house", "car", "kids", "dog"]

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
            
            
# how a user should pass a range of numbers

numOfBooks = [20]

with open('pipeline.txt', 'r') as f:
    f.write(numOfBooks)
    # randomizer will return a random number between 0 and numOfBooks
    
or

numOfBooks = [20]

with open('pipeline.text', 'r') as f:
    f.write(10, numOfBooks)
    # randomizer will return a random number between 10 and numOfBooks


num = [100]

with open('pipeline.txt', 'r') as f:
    f.write(10, num, 2) 
    # randomizer will return a random even number between 10 - 100
    
    
