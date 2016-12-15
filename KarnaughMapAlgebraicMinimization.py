#Algebraic Minimization with the Use of Karnaugh Map on a map with four variables.
#__author__:Mouzakitis Nikolaos,Crete 2016.
#Reading from a file named  "map.txt" locating in the same folder as your program.
#"map.txt",must contain 16 sequential binary digits . f.e: 0111010010010111 that
#will be used as the Karnaugh Map.

# v.2

def minimization(k):

    mini = []
    zero_cnt = 0
    prod = 1
    appended = 0  # used to count the times we ve applied a combination of squares in the map.
    print_k(k)    #printing on screen the Karnaugh Map,we are solving.

    for i in range(0, 16):

        prod *= k[i]

        if (k[i] == 0):

            zero_cnt += 1

    if (prod == 1):

        print("F(w,x,y,z) = 1\n")
        return

    if (zero_cnt == 16):

        print("F(w,x,y,z) = 0\n")
        return

    for i in range(0, 16):

        combo_value = 0  # works as flag to know the most squares for every midterm we can combine.
        combo_flag = 0

        if (k[i] == 0):

            combo.append(0)
            combo_flag = 1

        else:

            for j in range(0, 4):

                if (combo_value > 8):

                    break

                if (k[i] and k[driver_8[i][j][0] + i] and k[driver_8[i][j][1] + i] and k[driver_8[i][j][2] + i] and k[
                        driver_8[i][j][3] + i] and k[driver_8[i][j][4] + i] and k[driver_8[i][j][5] + i] and k[
                        driver_8[i][j][6] + i]):

                    combo_value = 8
                    combo.append(8)
                    combo_flag = 1
                    break

            for j in range(0, 6):

                if (combo_value > 4):

                    break

                if ((k[i] and k[driver_4[i][j][0] + i] and k[driver_4[i][j][1] + i] and k[driver_4[i][j][2] + i])):

                    combo_value = 4
                    combo.append(4)
                    combo_flag = 1
                    break

            for j in range(0, 4):

                if ((k[i] and k[i + driver_2[i][j]])):

                    if (combo_value > 2):

                        break

                    else:

                        combo.append(2)
                        combo_flag = 1
                        break

            if (combo_flag == 0):

                combo.append(1)
                # _calculating  free aces in the map and  position with highest combinable value
                #_free_aces aren't actually the free aces thought the program,just on the beggining.!!

    already_combined = []
    already_combined = combo
    free_aces = 0
    for element in k:

        if (element == 1):

            free_aces += 1

    k_max = combo[0]
    max_thesis = 0

    for i in range(0, 16):

        if (combo[i] > k_max):

            k_max = combo[i]
            max_thesis = i

    if (k_max == 1):

        print("The is no minimization on this function.")
        return
    #                                                        minimization code goes after here.
    map_copy = k
    solution = ""
    timer = 0

    while (max(already_combined) > 1):

        print("\nMINIMIZATION RUNS\n")

        for i in range(0, 16):

            if (   (combo[i] == 2 )   and (timer > 2)   ):

                for j in range(0, 4):

                    if ((k[i] and k[i + driver_2[i][j]]) and (already_combined[i] != 0) and zero[i + driver_2[i][j]] == 0 ): # and zero[i + driver_2[i][j]] == 0

                        duo = []
                        duo.append(i)
                        duo.append(i + driver_2[i][j])
                        duo.sort()
                        print("Combining the following squares: ", duo)
                        solution += solver(duo)
                        zero[i] = 1
                        zero[i + driver_2[i][j]] = 1
                        already_combined[duo[0]] = 0
                        already_combined[duo[1]] = 0
                        free_aces -= 2

            elif (combo[i] == 1):

                solution += solver([i])
                already_combined[i] = 0

        if (k_max == 8):  # minimization for eight squares combination.

            for j in range(0, 4):

                if (map_copy[max_thesis] and map_copy[driver_8[max_thesis][j][0] + max_thesis] and map_copy[
                        driver_8[max_thesis][j][1] + max_thesis] and map_copy[
                        driver_8[max_thesis][j][2] + max_thesis] and map_copy[
                        driver_8[max_thesis][j][3] + max_thesis] and map_copy[
                        driver_8[max_thesis][j][4] + max_thesis] and map_copy[
                        driver_8[max_thesis][j][5] + max_thesis] and map_copy[driver_8[max_thesis][j][6] + max_thesis]):

                    octo = []
                    octo.append(max_thesis)
                    octo.append(driver_8[max_thesis][j][0] + max_thesis)
                    octo.append(driver_8[max_thesis][j][1] + max_thesis)
                    octo.append(driver_8[max_thesis][j][2] + max_thesis)
                    octo.append(driver_8[max_thesis][j][3] + max_thesis)
                    octo.append(driver_8[max_thesis][j][4] + max_thesis)
                    octo.append(driver_8[max_thesis][j][5] + max_thesis)
                    octo.append(driver_8[max_thesis][j][6] + max_thesis)
                    octo.sort()
                    print("Combining the following squares  :", octo)
                    solution += solver(octo)
                    zero[max_thesis] = 1
                    zero[driver_8[max_thesis][j][0] + max_thesis] = 1
                    zero[driver_8[max_thesis][j][1] + max_thesis] = 1
                    zero[driver_8[max_thesis][j][2] + max_thesis] = 1
                    zero[driver_8[max_thesis][j][3] + max_thesis] = 1
                    zero[driver_8[max_thesis][j][4] + max_thesis] = 1
                    zero[driver_8[max_thesis][j][5] + max_thesis] = 1
                    zero[driver_8[max_thesis][j][6] + max_thesis] = 1
                    already_combined[octo[0]] = 0
                    already_combined[octo[1]] = 0
                    already_combined[octo[2]] = 0
                    already_combined[octo[3]] = 0
                    already_combined[octo[4]] = 0
                    already_combined[octo[5]] = 0
                    already_combined[octo[6]] = 0
                    already_combined[octo[7]] = 0
                    free_aces -= 8
                    break

        elif (k_max == 2):  # minimization for two squares combination.

            for j in range(0, 4):


                if ((map_copy[max_thesis] and map_copy[max_thesis + driver_2[max_thesis][j]]) and ((already_combined[max_thesis] != 0)  ) ):


                    duo = []
                    duo.append(max_thesis)
                    duo.append(max_thesis + driver_2[max_thesis][j])
                    duo.sort()
                    print("Combining the following squares: ", duo)
                    solution += solver(duo)
                    zero[max_thesis] = 1
                    zero[max_thesis + driver_2[max_thesis][j]] = 1
                    already_combined[duo[0]] = 0
                    already_combined[duo[1]] = 0
                    free_aces -= 2
                    break

        elif (k_max == 4):  # minimization for four squares combination.

            for j in range(0, 6):

                if ((map_copy[max_thesis] and map_copy[driver_4[max_thesis][j][0] + max_thesis] and map_copy[
                        driver_4[max_thesis][j][1] + max_thesis] and map_copy[
                        driver_4[max_thesis][j][2] + max_thesis])):

                    quatro = []
                    mini.append(
                        [max_thesis, driver_4[max_thesis][j][0] + max_thesis, driver_4[max_thesis][j][1] + max_thesis,
                         driver_4[max_thesis][j][2] + max_thesis])
                    appended += 1
                    quatro.append(max_thesis)
                    quatro.append(driver_4[max_thesis][j][0] + max_thesis)
                    quatro.append(driver_4[max_thesis][j][1] + max_thesis)
                    quatro.append(driver_4[max_thesis][j][2] + max_thesis)
                    print("Combining the following squares : ", quatro)
                    quatro.sort()
                    solution += solver(quatro)
                    zero[max_thesis] = 1
                    zero[driver_4[max_thesis][j][0] + max_thesis] = 1
                    zero[driver_4[max_thesis][j][1] + max_thesis] = 1
                    zero[driver_4[max_thesis][j][2] + max_thesis] = 1
                    already_combined[quatro[0]] = 0
                    already_combined[quatro[1]] = 0
                    already_combined[quatro[2]] = 0
                    already_combined[quatro[3]] = 0
                    free_aces -= 4
                    break


        if (max(already_combined) < 2):

            break

        timer += 1
        max_thesis = 0      # calculation of the new k_max and max_thesis
        k_max = already_combined[0]
        found_flag = 0

        for i in range(0, 16):

            if (zero[i] == 0):

                if (k_max < already_combined[i]):

                    k_max = already_combined[i]
                    max_thesis = i
                    found_flag = 1

            else:

                pass

        if (found_flag != 1):

            for i in range(0, 16):

                if (k_max < already_combined[i]):

                    k_max = already_combined[i]
                    max_thesis = i

                else:

                    pass

    print("\nMinimization Results:\n\nF(A,B,C,D)=", solution[:-2])

def solver(arg):

    sol = ""

    if (len(arg) == 1):

        if(arg == [0]):
            sol += " A'B'C'D' "
        elif (arg == [1]):
            sol += " A'B'C'D "
        elif (arg == [2]):
            sol += " A'B'CD' "
        elif (arg == [3]):
            sol += " A'B'CD "
        elif (arg == [4]):
            sol += " A'BC'D' "
        elif (arg == [5]):
            sol += " A'BC'D "
        elif (arg == [6]):
            sol += " A'BCD' "
        elif (arg == [7]):
            sol += " A'BCD "
        elif (arg == [8]):
            sol += " AB'C'D' "
        elif (arg == [9]):
            sol += " AB'C'D "
        elif (arg == [10]):
            sol += " AB'CD' "
        elif (arg == [11]):
            sol += " AB'CD "
        elif (arg == [12]):
            sol += " ABC'D' "
        elif (arg == [13]):
            sol += " ABC'D "
        elif (arg == [14]):
            sol += " ABCD' "
        elif (arg == [15]):
            sol += " ABCD "

    if (len(arg) == 2 ):

        if(arg == [0,1]):
            sol += " A'B'C' "
        elif(arg == [0,2]):
            sol += " A'B'D' "
        elif arg == [0, 4]:
            sol += " A'C'D' "
        elif(arg == [0,8]):
            sol += " B'C'D' "
        elif(arg == [1,3]):
            sol += " A'B'D "
        elif(arg == [1,5]):
            sol += " A'C'D "
        elif(arg == [1,9]):
            sol += " B'C'D "
        elif(arg == [2,3]):
            sol += " A'B'C "
        elif(arg == [3,7]):
            sol += " A'CD "
        elif(arg == [3,11]):
            sol += " B'CD "
        elif(arg == [2,6]):
            sol += " A'CD' "
        elif(arg == [2,10]):
            sol += " B'CD' "
        elif(arg == [4,5]):
            sol += " A'BC' "
        elif (arg == [4, 12]):
            sol += " BC'D' "
        elif(arg == [4,6]):
            sol += " A'BD' "
        elif(arg == [5,7]):
            sol += " A'BD "
        elif(arg == [5,13]):
            sol += " BC'D "
        elif(arg == [6,7]):
            sol += " A'BC "
        elif(arg == [7,15]):
            sol += " BCD "
        elif(arg == [6,14]):
            sol += " BCD' "
        elif(arg == [12,13]):
            sol += " ABC' "
        elif(arg == [8,12]):
            sol += " AC'D' "
        elif(arg == [12,14]):
            sol += " ABD' "
        elif(arg == [9,13]):
            sol += " AC'D "
        elif(arg == [13,15]):
            sol += " ABD "
        elif(arg == [11,15]):
            sol += " ACD "
        elif(arg == [14,15]):
            sol += " ABC "
        elif(arg == [10,14]):
            sol += " ACD' "
        elif (arg == [8, 9]):
            sol += " AB'C' "
        elif (arg == [8,10]):
            sol += " AB'D' "
        elif (arg == [9,11]):
            sol += " AB'D "
        elif (arg == [10, 11]):
            sol += " AB'C "

    if( len (arg) == 4):
        if( arg == [0,1,2,3]):
            sol += " A'B' "
        elif( arg == [0,1,4,5]):
            sol += " A'C' "
        elif( arg == [0,4,8,12]):
            sol += " C'D' "
        elif( arg == [0,1,8,9]):
            sol += " B'C'"
        elif( arg == [0,2,8,10]):
            sol += " B'D' "
        elif(arg == [0,2,4,6]):
            sol += " A'D' "
        elif( arg == [1,5,9,13]):
            sol += " C'D "
        elif( arg == [1,3,5,7]):
            sol += " A'D "
        elif(arg == [1,3,9,11]):
            sol += " B'D "
        elif(arg == [2,3,6,7]):
            sol += " A'C "
        elif(arg == [2,3,10,11]):
            sol += " B'C "
        elif(arg == [3,7,11,15]):
            sol += " CD "
        elif(arg == [2,6,10,14]):
            sol += " CD' "
        elif(arg == [4,5,6,7]):
            sol += " A'B "
        elif(arg == [4,5,12,13]):
            sol += " BC' "
        elif(arg == [4,6,12,14]):
            sol += " BD' "
        elif(arg == [5,7,13,15]):
            sol += " BD "
        elif(arg == [6,7,14,15]):
            sol += " BC "
        elif(arg == [12,13,14,15]):
            sol += " AB "
        elif(arg == [8,9,12,13]):
            sol += " AC' "
        elif(arg == [8,10,12,14]):
            sol += " AD' "
        elif(arg == [9,11,13,15]):
            sol += " AD "
        elif(arg == [10,11,14,15]):
            sol += " AC "
        elif(arg == [8,9,10,11]):
            sol += " AB' "

    if (len(arg) == 8):
        if(arg == [0,1,2,3,4,5,6,7]):
            sol += " A' "
        elif(arg == [0,1,2,3,8,9,10,11]):
            sol += " B' "
        elif(arg == [0,2,4,6,8,10,12,14]):
            sol += " D' "
        elif(arg == [0,1,4,5,8,9,12,13]):
            sol += " C' "
        elif(arg == [1,3,5,7,9,11,13,15]):
            sol += " D "
        elif(arg == [4,5,6,7,12,13,14,15]):
            sol += " B "
        elif(arg == [2,3,6,7,10,11,14,15]):
            sol += " C "
        elif(arg == [8,9,10,11,12,13,14,15]):
            sol += " A "


    return sol + " + "

def print_k(k):

    line1 = [0,1,3,2]
    line2 = [4,5,7,6]
    line3 = [12,13,15,14]
    line4 = [8,9,11,10]
    print("KARNAUGH   MAP   DISPLAY\n")
    print((str)(k[line1[0]]) +"\t"+(str)(k[line1[1]])+"\t"+(str)(k[line1[2]])+"\t"+(str)(k[line1[3]])+"\n")
    print((str)(k[line2[0]]) +"\t"+(str)(k[line2[1]])+"\t"+(str)(k[line2[2]])+"\t"+(str)(k[line2[3]])+"\n")
    print((str)(k[line3[0]]) +"\t"+(str)(k[line3[1]])+"\t"+(str)(k[line3[2]])+"\t"+(str)(k[line3[3]])+"\n")
    print((str)(k[line4[0]]) +"\t"+(str)(k[line4[1]])+"\t"+(str)(k[line4[2]])+"\t"+(str)(k[line4[3]])+"\n")

#________
#Program.
zero = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
k_map = []
combo = []
free_aces = 0
solution = ""
driver_2 = []
driver_4 = []
driver_8 = []
#-------------SETTING UP THE LIST driver_2------------------------------------------------------
driver_2.append([1, 2, 4, 8])
driver_2.append([-1, 2, 4, 8])
driver_2.append([1, -2, 4, 8])
driver_2.append([-1, -2, 4, 8])
driver_2.append([-4,1, 2, 8])
driver_2.append([-1,-4,2,8])
driver_2.append([-2, -4,1,8])
driver_2.append([-4, -2, -1, 8])
driver_2.append([ -8,1, 2, 4])
driver_2.append([ -8,-1, 2, 4])
driver_2.append([-8,-2,1,4])
driver_2.append([-8,-2,-1, 4])
driver_2.append([-8,-4,1, 2])
driver_2.append([-8,-4,-1, 2])
driver_2.append([-8,-4,-2,1])
driver_2.append([-8,-4,-2,-1])
#-------------SETTING UP THE LIST driver_4------------------------------------------------------
driver_4.append([ [1,2,3],[4,8,12],[1,4,5],[2,4,6],[2,8,10],[1,8,9] ])
driver_4.append([ [-1,1,2],[4,8,12],[-1,3,4],[2,4,6],[-1,7,8],[2,8,10] ])
driver_4.append([ [-2,-1,1],[4,8,12],[-2,6,8],[1,4,5],[-2,2,4],[1,8,9] ])
driver_4.append([ [-1,-2,-3],[4,8,12],[-1,3,4],[-2,2,4],[-2,6,8],[-1,7,8] ])
driver_4.append([ [1,2,3],[-4,4,8],[1,8,9],[-4,-3,1],[-4,-2,2],[2,8,10] ])
driver_4.append([ [-1,1,2],[-4,4,8],[2,8,10],[-4,-2,2],[-5,-4,-1],[-1,7,8] ])
driver_4.append([ [-4,4,8],[-2,-1,1],[-4,-3,1],[1,8,9],[-2,6,8],[-6,-4,-2] ])
driver_4.append([ [-4,4,8],[-3,-2,-1],[-2,6,8],[-6,-4,-2],[-5,-4,-1],[-1,7,8] ])
driver_4.append([ [-8,-4,4],[1,2,3],[-8,-6,2],[6,4,2],[5,4,1],[-8,-7,1] ])
driver_4.append([ [-8,-4,4],[-1,1,2],[-1,3,4],[-9,-8,-1],[-8,-6,2],[6,4,2] ])
driver_4.append([ [-2,-1,1],[-8,-4,4],[-10,-8,-2],[-2,2,4],[1,4,5],[-8,-7,1] ])
driver_4.append([ [-3,-2,-1],[-4,-8,4],[-9,-8,-1],[-1,3,4],[-2,2,4],[-10,-8,-2] ])
driver_4.append([ [1,2,3],[-12,-8,-4],[-4,-3,1],[-4,-2,2],[-8,-6,2],[-8,-7,1] ])
driver_4.append([ [-1,1,2],[-12,-8,-4],[-8,-6,2],[-5,-4,-1],[-4,-2,2],[-9,-8,-1] ])
driver_4.append([ [1,-1,-2],[-12,-8,-4],[1,-3,-4],[-6,-4,-2],[1,-7,-8],[-10,-8,-2] ])
driver_4.append([ [-3,-2,-1],[-12,-8,-4],[-5,-4,-1],[-6,-4,-2],[-10,-8,-2],[-9,-8,-1] ])
#-------------SETTING UP THE LIST driver_8------------------------------------------------------
driver_8.append([ [1,2,3,4,5,6,7],[1,2,3,8,9,10,11],[1,4,5,8,9,12,13],[2,4,6,8,10,12,14] ] )
driver_8.append([ [-1,1,2,3,4,5,6],[-1,1,2,7,8,9,10],[-1,3,4,7,8,11,12],[2,4,6,8,10,12,14] ] )
driver_8.append([ [-2,-1,1,2,3,4,5],[-2,-1,1,6,7,8,9],[1,4,5,8,9,12,13],[-2,2,4,6,8,10,12] ] )
driver_8.append([ [-3,-2,-1,1,2,3,4],[-3,-2,-1,5,6,7,8],[-2,2,4,6,8,10,12],[-1,3,4,7,8,11,12] ] )
driver_8.append([ [-4,-3,-2,-1,1,2,3],[1,2,3,8,9,10,11],[-4,-2,2,4,6,8,10],[-4,-3,1,4,5,8,9] ] )
driver_8.append([ [-5,-4,-3,-2,-1,1,2],[-1,1,2,7,8,9,10],[-5,-4,-1,3,4,7,8],[-4,-2,2,4,6,8,10] ] )
driver_8.append([ [-6,-5,-4,-3,-2,-1,1],[-2,-1,1,6,7,8,9],[-4,-3,1,4,5,8,9],[-6,-4,-2,2,4,6,8] ] )
driver_8.append([ [-7,-6,-5,-4,-3,-2,-1],[-3,-2,-1,5,6,7,8],[-5,-4,-1,3,4,7,8],[-6,-4,-2,2,4,6,8] ] )
driver_8.append([ [7,6,5,4,3,2,1],[3,2,1,-5,-6,-7,-8],[5,4,1,-3,-4,-7,-8],[6,4,2,-2,-4,-6,-8] ] )
driver_8.append([ [6,5,4,3,2,1,-1],[2,1,-1,-6,-7,-8,-9],[4,3,-1,-4,-5,-8,-9],[6,4,2,-2,-4,-6,-8] ] )
driver_8.append([ [5,4,3,2,1,-1,-2],[1,-1,-2,-7,-8,-9,-10],[5,4,1,-3,-4,-7,-8],[4,2,-2,-4,-6,-8,-10] ] )
driver_8.append([ [4,3,2,1,-1,-2,-3],[-1,-2,-3,-8,-9,-10,-11],[4,2,-2,-4,-6,-8,-10],[4,3,-1,-4,-5,-8,-9] ] )
driver_8.append([ [3,2,1,-1,-2,-3,-4],[3,2,1,-5,-6,-7,-8],[2,-2,-4,-6,-8,-10,-12],[1,-3,-4,-7,-8,-11,-12] ] )
driver_8.append([ [2,1,-1,-2,-3,-4,-5],[2,1,-1,-6,-7,-8,-9],[-1,-4,-5,-8,-9,-12,-13],[2,-2,-4,-6,-8,-10,-12] ] )
driver_8.append([ [1,-1,-2,-3,-4,-5,-6],[1,-1,-2,-7,-8,-9,-10],[1,-3,-4,-7,-8,-11,-12],[-2,-4,-6,-8,-10,-12,-14] ] )
driver_8.append([ [-1,-2,-3,-4,-5,-6,-7],[-1,-2,-3,-8,-9,-10,-11],[-1,-4,-5,-8,-9,-12,-13],[-2,-4,-6,-8,-10,-12,-14] ] )
#-----------------------------------------------------------------------------------------------

'''  #GETTING INPUT FROM KEABORD CODE
for i in range(0,16):
    midterm = (int)(input('Enter the ['+(str)(i)+"] midterm.\n"))
    k_map.append(midterm)
'''
try:
    fd = open("map.txt","r")
    line = fd.readline()
    for i in line:
        k_map.append( (int) (i))


    minimization(k_map)
except IOError as err:
    print("Error occured:%s"%(str)(err))

finally:
    if 'fd' in locals():
        fd.close()
