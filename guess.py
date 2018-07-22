cube =  float(input("Enter value to search for is cube root: "))

epsilon = 0.00000000001
num_guesses = 0

if (cube >=1):
    low = 0
    high = cube
    guess = (high+low)/2.0

    while(abs(guess**3 - cube) >= epsilon):
        print("guess: "+str(guess))
        if guess**3 < cube:
            low = guess
        else:
            high = guess
        guess = (high+low)/2.0
        num_guesses+=1

elif(cube <= -1):
    low = cube 
    high = 0 
    guess = (high+low)/2.0

    while(abs(guess**3 - cube) >= epsilon):
        print("guess: "+str(guess))
        if guess**3 < cube:
            low = guess
        else:
            high = guess
        guess = (high+low)/2.0
        num_guesses+=1

elif( (cube < 1) and (cube >0)):
    low = cube
    high = 1
    guess = (high + low)/2.0

    while(abs(guess**3-cube) >= epsilon):
        print("guess: "+ str(guess))
        if guess**3 > cube:
           high = guess  
        else:
           low = guess 
        guess = (high + low)/2.0
        num_guesses+=1

elif( (cube < 0) and (cube > -1) ):
   
    low = -1
    high = cube 
    guess = (high + low)/2.0

    while(abs(guess**3-cube) >= epsilon):
        print("guess: "+ str(guess))
        if guess**3 > cube:
           high = guess  
        else:
           low = guess 
        guess = (high + low)/2.0
        num_guesses+=1

elif(cube == 0):
    guess = 0
    num_guesses+=1

print("Num guesses: " + str(num_guesses))
print(str(guess) + " is close to the cube root of "+str(cube))
