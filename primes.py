import math

#Module with functions on prime numbers : Mouzakitis Nikolaos,Crete,2016.

#isPrime
#areTwins
#primesSum
#primesInRange

#isPrime(k): returns 1 if the number is prime,otherwise return value is 0.
def isPrime(k) :

    cnt = 0
    if( k == 0):
        return 0
    elif ( k == 1 ):
        return 0
    elif ( k == 2):
        return 1
    else:
        for t in range ( 2 , math.ceil( k/2 + 1) ): # from definition of primes,there is no divisor of K between ( 2 , [k/2] )
            if(k%t == 0):
                cnt = cnt + 1
        if (cnt != 0):
            return 0
        else:
            return 1


#primesInRange(init,final): returns the number of primes in the given range(init,final)
def primesInRange(init,final):

    p_cnt = 0
    
    for i in range(init,final + 1):

        if(isPrime(i)):

            p_cnt += 1

    return p_cnt


#areTwins(a,b): returns 1 if the arguments form a prime tuplet.0 otherwise.
def areTwins(a,b):
    if( (a - b != 2 ) and (b - a != 2) ):
        return 0
    else:
        if(isPrime(a) and isPrime(b)):
            return 1
        else:
            return 0




#calculates the sum of all the primes within' the given range(init,final)
def primesSum(init,final):

    psum = 0

    for i in range(init,final+1):

        if(isPrime(i)):

            psum += i

    return psum
