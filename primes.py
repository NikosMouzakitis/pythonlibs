#*#***************************************************
#*#***************************************************
#*# __________________primes.py______________________*                                           
#*#                                                  *                                                   
#*#   Module with functions on prime numbers.        *                         
#*#                                  [ : ]           *                                                   
#*#__________________________________________________*
#*#_________author: __Mouzakitis Nikolaos,Crete,2016.* 
#*#                                                  *
#*#             Implemented functions:               *                                    
#*#                                                  *                                               
#*#                                                  *                                               
#*#     1.isPrime                                    *                                         
#*#     _________                                    *                                             
#*#     2.primesInRange                              *                                
#*#     _______________                              *                                                 
#*#     3.areTwins                                   *                                          
#*#     __________                                   *                                                 
#*#     4.primesSum                                  *                                          
#*#     ___________                                  *                                                   
#*#     5.primeFactorization                         *                                  
#*#     ____________________                         *                                             
#*#     6.twinsSum                                   *                                           
#*#     __________                                   *                                                    
#*#     7.twinsInRange                               *                                         
#*#     ______________                               *
#*#     8.minimum                                    *
#*#     _________                                    *
#*#     9.gcd                                        *
#*#     ______                                       *
#*#     10.maximum                                   *
#*#     __________                                   *
#*#     11.isMersenne                                *
#*#     _____________                                *
#*#***************************************************
#*#***************************************************

import math

#isPrime(k): returns 1 if the number is prime,otherwise return value is 0.
def isPrime(k) :
    '''returns 1 if the number is prime,otherwise return value is 0.
     argument must be an integer'''
    cnt = 0

    if(k <= 1):
        return 0
    elif ( k == 2):
        return 1
    else:
        for t in range ( 2 , math.ceil( k /2 + 1) ): # from definition of primes,there is no divisor of K between ( 2 , [k/2] )
            if(k%t == 0):
                cnt = cnt + 1
        if (cnt != 0):
            return 0
        else:
            return 1


#primesInRange(init,final): returns the number of primes in the given range(init,final)
def primesInRange(init,final):

    ''' primesInRange(init,final): returns the number of primes in the given range(init,final)'''
    p_cnt = 0
    
    for i in range(init,final + 1):

        if(isPrime(i)):

            p_cnt += 1

    return p_cnt


#areTwins(a,b): returns 1 if the arguments form a prime tuplet.0 otherwise.
def areTwins(a,b):

    ''' areTwins(a,b): returns 1 if the arguments form a prime tuplet.0 otherwise.'''
    
    if( (a - b != 2 ) and (b - a != 2) ):
        return 0
    else:
        if(isPrime(a) and isPrime(b)):
            return 1
        else:
            return 0




#calculates the sum of all the primes within' the given range(init,final)
def primesSum(init,final):

    '''calculates the sum of all the primes within' the given range(init,final)'''

    psum = 0

    for i in range(init,final+1):

        if(isPrime(i)):

            psum += i

    return psum

#primeFactorization. Returns a list with the prime factorization
#of the given natural number.Returns (-1) on false input.
def primeFactorization(n):

    '''primeFactorization. Returns a list with the prime factorization
    of the given natural number.Returns (-1) on false input.'''


    if(n < 0):
        print("not a natural number.invalid input.\n")
        return -1

    prime_list = []
    factorization = []
        
    
    for i in range(2, math.ceil(n/2) +1 ):
        if(isPrime(i)):
            prime_list.append(i)

    lenght = len(prime_list)

    if(isPrime(n)):
        factorization.append(n)
    
    else:
     
        for i in range(0, lenght ):
       
        
            while( ( (n % prime_list[i]) == 0) and (n != 1)) :
        
                factorization.append( int(prime_list [i] ))
                n = int( n  / prime_list[i] )

    return factorization


#twinsSum(init,final).Calculates the sum of all the twin primes within' the given range(init,final)
def twinsSum(init,final):

    '''twinsSum(init,final).Calculates the sum of all the twin primes within' the given range(init,final)'''


    tsum = 0

    for i in range(init,final + 1):

        if(isPrime(i) and isPrime(i+2)):
            tsum += 2*i + 2

    if( init < 3):

        if(isPrime(final + 2)):
            return (tsum - (final + 2) - 5)
        
        else:
            return (tsum - 5)

    else:

        if(isPrime(final + 2)):
            return (tsum - (final + 2))
        
        else:
            return (tsum)



#twinsInRange(init,final).Calculates how many individual twin primes reside in the given range(init,final)
#If (final,final + 2) are also prime twins,function will count final in the return value.
def twinsInRange(init,final):

    '''twinsInRange(init,final).Calculates how many individual twin primes reside in the given range(init,final)
    If (final,final + 2) are also prime twins,function will count final in the return value.'''


    counter = 0
    
    for i in range(init,final + 1):

        if(areTwins(i,i+2)):
            counter +=2

    if(init <= 3):
        return counter - 1
    else:
        return counter

#Returns the minimum value between two numbers(even if they are equal,value is returned).
def minimum(a,b):
    
    '''#Returns the minimum value between two numbers(even if they are equal,value is returned).'''
    if(a > b ):
        return b
    else:
        return a

#Greatest common divisor of natural numbers a,b.Returns (-1) if any of the two inputs ain't a natural number.
def gcd(a,b):

    '''Greatest common divisor of natural numbers a,b.'''
    if((a < 0) or (b < 0) ):
        return -1
    elif(isPrime(a) and isPrime(b)):
        return 1
    else:
        k = minimum(a,b)
        for i in range(1,k+1):
            if( (a % i == 0) and (b % i == 0) ):
                gcd = i
    return gcd


#Returns the maximum value between two numbers(even if they are equal,value is returned).
def maximum(a,b):
    
    '''Returns the maximum value between two numbers(even if they are equal,value is returned).'''
    if(a > b ):
        return a
    else:
        return b

#isMersenne(a) Returns 1 if the input natural number is Mersenne prime.Zero otherwise.
def isMersenne(a):
    '''Returns 1 if the input natural number is Mersenne prime.Zero otherwise.'''

    limit = int(a / 2) + 1
    value = 1

    if(  isPrime(a) == 0 ):
        return 0
    
    for i in range(1,limit + 1):
        value = value * 2
        if( ( (value - 1) == a ) and isPrime(a) ):
            return 1

    return 0
