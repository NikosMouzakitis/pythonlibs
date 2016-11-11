    #____________________NEWTON_RAPHSON METHOD___________________________#
    #____Solution_of__F(x) = 0 __ with Newton-Raphson's ____ algorithm.__#
    #____________________________________________________________________#

l = []                                               #list thatt will hold all possible positive values close to the root of function.
applied_results = []                                 #finally created list holding the results you get.

def newtonRaphsonInitialization(lb,ub):              #Upperbound,lowerBound
        
    for i in range(lb,ub+1):
        acc = 0.9999
        if(function_to_Solve(i) * function_to_Solve(i + acc) <= 0):
            if(function_to_Solve(i) * function_to_Solve(i + acc) == 0):
                if(function_to_Solve(i) == 0):
                    l.append(i)
                else:
                    l.append(i+acc)
            else:
                if(function_to_Solve(i) > 0):
                    l.append(i)
                else:
                    l.append(i+acc)    
                               
def function_to_Solve(x):
    value = 4*x*x - 9
    return (float) (value)

def  differential(x):
    value = 8*x
    return (float)(value)

def newtonRaphson(x):

    x_next =x - (float)(function_to_Solve(x)) / differential(x)    
    return x_next    
#  *********************************************************************************   #
lower = (int)(input("Enter the lower bound of the search:\n"))
upper = (int)(input("Enter the  upper bound of the search:\n"))
repeat = (int)(input('Enter the times you want to apply Newton - Raphson\'s method.'))
newtonRaphsonInitialization(lower,upper)

print("Detected {a} points in the space[{b},{c}]".format ( a = len(l),b = lower,c = upper ) )
print(l)
                                                    
for i in l:                                         #Implementing the algorithm for every solution.
    y = i
    
    for t in range(1,repeat):

        tmp = newtonRaphson(y)
        print('implementing algorithm')
        y=tmp
        
    applied_results.append(y)                       #storing results in result list.

print("Final results:\n ")
print(applied_results)
#          ********************************************************************************
