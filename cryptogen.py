#|++++++++++++++++++++++++++++++++++++++++|
#|  +   +   +   +   +   +   +   +   +   + |
#|++++++++++++++++++++++++++++++++++++++++|
#|_______________cryptogen.py_____________|
#|++++++++++++++++++++++++++++++++++++++++|
#|  +   +   +   +   +   +   +   +   +   + |
#|++++++++++++++++++++++++++++++++++++++++|
#|Module with implemented cryptographic   |
#|  functions                             |
#|  +   +   +   +   +   +   +   +   +   + |
#|                                        |
#|________________________________________|
#|______________author:Mouzakitis_Nikolaos|
#|___Crete 2016___________________________|
#|                                        |
#|  +   +   +   +   +   +   +   +   +   + |
#|                                        |
#|__i)letFreqAnalyse______________________|
#|  +   +   +   +   +   +   +   +   +   + |
#|                                        |
#|_ii)isLatin_____________________________|
#|  +   +   +   +   +   +   +   +   +   + |
#|                                        |
#|iii)ceasarEncode________________________|
#|  +   +   +   +   +   +   +   +   +   + |
#|                                        |
#|_iv)ceasarDecode________________________|
#|  +   +   +   +   +   +   +   +   +   + |
#|                                        |
#|  +   +   +   +   +   +   +   +   +   + |
#|________________________________________|
'''Python module
       implementing
       some basic
       cryptographic
       functions'''


alphabet_sm=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet_big=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


#letFreqAnalyse()
def letFreqAnalyse(fp):
    ''' letFreqAnalyse(fp):

    Takes as an argument a file descriptor which has
    just been opened a file and performs a letter
    frequency analysis on its data.'''

    letters_sum=0
    alpha_percent=[]
    
    alphabet_count=[]

    for i in range(1,27):
        alphabet_count.append(0)    #setting alphabet_count list to zeros.

    for i in range(1,27):
        alpha_percent.append(0) #setting alpha_percent list to zeros.

    for line in fp:
        for letter in line:
            for i in range(0,26):
                if(  (letter == alphabet_sm[i]) or (letter == alphabet_big[i])   ):
                    alphabet_count[i] +=1

    for i in range(0,26):
            letters_sum += alphabet_count[i]    #calculating the total sum of letters in the file.

    for i in range(0,26):
    
        value = (float) (( alphabet_count[i] / letters_sum) *100 )
        
        alpha_percent[i] = value 
        
    print("\n\nLETTER     FREQUENCY    ANALYSIS\n")
    print("letter      frequency/cent\n")    
    for i in range(0,26):
        print(alphabet_big[i] + " :\t\t %.3f"%(alpha_percent[i]))

#isLatin()
def isLatin(k):
    '''isLatin(k) : returns 1 if the argument
    is a latin character either capital or small.'''
    if( (k>='a' and k <='z') or (k>='A' and k <='Z')    ):
        return 1
    else:
        return 0

#Ceasar_encode()
def ceasarEncode(message,shift):
    ''' Ceasar's cipher encryption.'''
    encrypted = [] 
    for letter in message:   
        if (isLatin(letter)):
            
            k = 0
            while(k<=25):
                if (    (letter!=alphabet_sm[k])   and (letter !=alphabet_big[k])   ):
                    k+=1
                else:
                    if(k+shift > 25):
                        t = k + shift -26
                        encrypted.append(alphabet_sm[t])
                    else:
                        encrypted.append(alphabet_sm[k+shift])
                    break
    encoded = ""
    for index in encrypted:
        encoded +=index
    print("Encryption:\t",encoded)
    
#Ceasar_decode()
def ceasarDecode(message,shift):
    ''' Ceasar's cipher decryption.'''
    decrypted = []
    for letter in message:
        if(isLatin(letter)):
            k = 0
            while(k <=25):
                if ( (letter!=alphabet_sm[k])   and (letter !=alphabet_big[k]) ):
                    k+=1
                else:
                    if(k+shift > 25):
                        t = k + shift -26
                        decrypted.append(alphabet_sm[t])
                    else:
                        decrypted.append(alphabet_sm[k+shift])
                    break
    decoded = ""
    for index in decrypted:
        decoded+=index
    print("Decryption:\t",decoded)
