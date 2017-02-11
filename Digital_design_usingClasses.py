####_----------------------------------_#
####_----------------------------------_#
####    Digital Design                  #
####    classes and implementation      #
####    of basic boolean functions.     #
####____________________________________#
####    Following the example you can   #
####    created the circuit you need    #
####    and work ot the truth table.    # 
####____________________________________#
####    February 2017                   #
####    Mouzakitis Nikolaos,Crete.      #
####_----------------------------------_#

class Nor_2():
    
    outSignal = 0

    def insert(self,a,b):

        self.outSignal = NOT(a) and NOT(b) 

        return self.outSignal

class Nand_2():

    outSignal = 0

    def insert(self,a,b):

        self.outSignal = NOT(a) or NOT(b)

        return self.outSignal

class Xor_2():
    
    outSignal = 0

    def insert(self,a,b):

        self.outSignal = ( a and ( NOT(b) ) ) or ( ( NOT(a) ) and b )

        return self.outSignal

class Xnor_2():
    
    outSignal = 0

    def insert(self,a,b):

        self.outSignal = ( NOT(a) and NOT(b) ) or ( a and b )

        return self.outSignal

   
class Or_2():
     
    outSignal = 0
    
    def insert(self,a,b):

        self.outSignal = a or b
        
        return self.outSignal
    
class Or_3():

    outSignal = 0
    
    def insert(self,a,b,c):

        self.outSignal = a or b or c
        
        return self.outSignal

class Or_4():
     
    outSignal = 0
    
    def insert(self,a,b,c,d):

        self.outSignal = a or b or c or d
        
        return self.outSignal


class And_2():
     
    outSignal = 0
    
    def insert(self,a,b):

        self.outSignal = a and b
        
        return self.outSignal
    
class And_3():

    outSignal = 0
    
    def insert(self,a,b,c):

        self.outSignal = a and b and c
        
        return self.outSignal
    
class And_4():

    outSignal = 0
    
    def insert(self,a,b,c,d):

        self.outSignal = a and b and c and d
        
        return self.outSignal
    

def NOT(s):

    if ( s ):

        return 0
    else:

        return 1

        
def formated(tmp,no):
    return_list =[]
    x = tmp[2:]

    offset = no - len(x)

    if ( offset != 0):

        for i in range(0,offset):
        
            return_list.append(0)


    for i in range(0,no - offset):

        return_list.append(int(x[i]))
    
    return (return_list)




number_of_inputs = 4

inputs_list = []

for i in range(0,number_of_inputs**2):

    tmp = bin(i)

    inputs_list.append(formated(tmp,number_of_inputs))

    

 


print("TRUTH TABLE")

for i in range(0,number_of_inputs**2):

    g1 = Or_3()
    w = g1.insert(inputs_list[i][0],inputs_list[i][1],inputs_list[i][2])
    g2 = And_2()
    x = g2.insert(inputs_list[i][1],inputs_list[i][3])

    g3 = Nand_2()
    f = g3.insert(w,x)

    print("(%d,%d,%d,%d)  %d"%(inputs_list[i][0],inputs_list[i][1],inputs_list[i][2],inputs_list[i][3],f ) )
 
