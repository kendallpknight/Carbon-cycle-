import numpy as np
import matplotlib.pyplot as plt
# h will be .2 for now, might add tkinter or slider to change
#These calculation i feel decent about. just where each
#comapartment equals its intial value + the changes, im not 100% on 

def n1calc(n1val, n2val, n3val, n4val, n5val, n6val, n7val, h):
    global k12,k21,k32,k23,k17,k16,k14,k41,k64,k54,k65,k76
    newval = n1val - (h *(n1val - (k21* n1val)-(#needs the weird flow f41
        )
                          +(#weird flow f12
                              )
                              + (k17 * n7val) +
                          (k16 * n6val) + (k14 * n4val)))
    return newval
def n2calc(n1val, n2val, n3val, n4val, n5val, n6val, n7val, h):
    global k12,k21,k32,k23,k17,k16,k14,k41,k64,k54,k65,k76
    newval = n2val - (h *(n2val - (#needs f12
        )
                          - (k32 * n2val)
                          + (k21 * n1val) + (k23 * n3val)))
    return newval
def n3calc(n1val, n2val, n3val, n4val, n5val, n6val, n7val, h):
    global k12,k21,k32,k23,k17,k16,k14,k41,k64,k54,k65,k76
    newval = n3val - (h *(n3val -(k23 * n3val)+(k32 * n2val)))
    return newval
def n4calc(n1val, n2val, n3val, n4val, n5val, n6val, n7val, h):
    global k12,k21,k32,k23,k17,k16,k14,k41,k64,k54,k65,k76
    newval = n4val - (h *(n4val - (k14 * n4val) - (k64 * n4val)
                          - (k54 * n4val) + (#f41
                              )))
    return newval
def n5calc(n1val, n2val, n3val, n4val, n5val, n6val, n7val, h):
    global k12,k21,k32,k23,k17,k16,k14,k41,k64,k54,k65,k76
    newval = n5val - (h *(n5val - (k65 * n5val) + (k54 * n4val)))
    return newval
def n6calc(n1val, n2val, n3val, n4val, n5val, n6val, n7val, h):
    global k12,k21,k32,k23,k17,k16,k14,k41,k64,k54,k65,k76
    newval = n6val - (h *(n6val - (k16 * n6val) - (k76 * n6val)
                          + (k65 * n5val) + (k64 * n4val)))
    return newval
def n7calc(n1val, n2val, n3val, n4val, n5val, n6val, n7val, h):
    global k12,k21,k32,k23,k17,k16,k14,k41,k64,k54,k65,k76
    newval = n7val - (h *(n7val - (k17 * n7val) + (k76 * n6val)))
    return newval

#k calculations
k12 = 100/1000 # this is not right 
k21 = 100/700 
k32 = (100/3)/1000
k23 = (100/3)/36000
k17 = 2/1500
k16 = 53/60
k14 = 55/130
k41 = 110/700 #this is not right. Both ^ of these need the weird equations
                      #that means n1, n2 and n4 calc are wrong as well
k64 = 40/130
k54 = 15/130
k65 = 15/700
k76 = 2/60
#array creation
t = np.arange(0,117,.2)
n1 = np.zeros(len(t + 1))
n2 = n1
n3 = n1
n4 = n1
n5 = n1
n6 = n1
n7 = n1
#intial values for each comapartment
n1[0] = 700
n2[0] = 1000
n3[0] = 36000
n4[0] = 130
n5[0] = 700
n6[0] = 60
n7[0] = 1500
for i in range(len(t) + 1):
    n1[i+1] = n1calc(n1[i],n2[i],n3[i],n4[i],n5[i],n6[i],n7[i],h)
    n2[i+1] = n2calc(n1[i],n2[i],n3[i],n4[i],n5[i],n6[i],n7[i],h)
    n3[i+1] = n3calc(n1[i],n2[i],n3[i],n4[i],n5[i],n6[i],n7[i],h)
    n4[i+1] = n4calc(n1[i],n2[i],n3[i],n4[i],n5[i],n6[i],n7[i],h)
    n5[i+1] = n5calc(n1[i],n2[i],n3[i],n4[i],n5[i],n6[i],n7[i],h)
    n6[i+1] = n6calc(n1[i],n2[i],n3[i],n4[i],n5[i],n6[i],n7[i],h)
    n7[i+1] = n7calc(n1[i],n2[i],n3[i],n4[i],n5[i],n6[i],n7[i],h)
plt.plot(t,n1)
plt.plot(t,n2)
plt.plot(t,n3)
plt.plot(t,n4)
plt.plot(t,n5)
plt.plot(t,n6)
plt.plot(t,n7)
plt.show()
