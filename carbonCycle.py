import numpy as np
import matplotlib.pyplot as plt
#the euler functions for each compartment (yn = yn-1 + h*f(x))
def n1calc(n1val, n2val, n3val, n4val, n5val, n6val, n7val,time, h):
    global k12,k21,k32,k23,k17,k16,k14,k41,k64,k54,k65,k76
    human_add = ( .5* (np.e**(.03*time)))
    
    newval = n1val + (h *((n2val - 900)-(k21* n1val)-(k41 * n4val*(1 + .1*np.log(n1val/700))) + (k17 * n7val) +  (k16 * n6val) + (k14 * n4val)+ human_add  ))
    #print(newval,time, "n2 = ",n2val, "n1 = ",n1val,"n4=",n4val,"n7=",n7val,"n6=",n6val)
    return newval
def n2calc(n1val, n2val, n3val, n4val, n5val, n6val, n7val, h):
    global k12,k21,k32,k23,k17,k16,k14,k41,k64,k54,k65,k76
    newval = n2val + (h *((k21 * n1val)-(n2val - 900) - (k32 * n2val)+   (k23 * n3val)))
    return newval
def n3calc(n1val, n2val, n3val, n4val, n5val, n6val, n7val, h):
    global k12,k21,k32,k23,k17,k16,k14,k41,k64,k54,k65,k76
    newval = n3val + (h *( (k32 * n2val)-(k23 * n3val)))
    return newval
def n4calc(n1val, n2val, n3val, n4val, n5val, n6val, n7val, h):
    global k12,k21,k32,k23,k17,k16,k14,k41,k64,k54,k65,k76
    newval = n4val + (h *((k41 * n4val*( 1 + .1*np.log(n1val/700)))-(k14 * n4val) - (k64 * n4val) - (k54 * n4val) ))
    return newval
def n5calc(n1val, n2val, n3val, n4val, n5val, n6val, n7val, h):
    global k12,k21,k32,k23,k17,k16,k14,k41,k64,k54,k65,k76
    newval = n5val + (h *(((k54 * n4val) -(k65 * n5val))))
    return newval
def n6calc(n1val, n2val, n3val, n4val, n5val, n6val, n7val, h):
    global k12,k21,k32,k23,k17,k16,k14,k41,k64,k54,k65,k76
    newval = n6val + (h *((k65 * n5val)-(k16 * n6val) - (k76 * n6val)  + (k64 * n4val)))
    return newval
def n7calc(n1val, n2val, n3val, n4val, n5val, n6val, n7val,time, h):
    global k12,k21,k32,k23,k17,k16,k14,k41,k64,k54,k65,k76
    human_add = (.5 * (np.e**(.03*time)))
    newval = n7val + (h *((k76 * n6val) -(k17 * n7val) ))
    return newval

#k calculations
#computed from model given
k12 = 100/1000 
k21 = 100/700 
k32 = (100/3)/1000
k23 = (100/3)/36000
k17 = 2/1500
k16 = 53/60
k14 = 55/130
k41 = 110/130 
k64 = 40/130
k54 = 15/130
k65 = 15/700
k76 = 2/60
#array creation
h = .1
t = np.arange(0,120,.1)
n1 = np.ones(len(t))
n2 = np.zeros(len(t))
n3 = np.zeros(len(t))
n4 = np.zeros(len(t))
n5 = np.zeros(len(t))
n6 = np.zeros(len(t))
n7 = np.zeros(len(t))
#intial values for each compartment
n1[0] = 700
n2[0] = 1000
n3[0] = 36000
n4[0] = 130
n5[0] = 700
n6[0] = 60
n7[0] = 1500
for i in range(len(t) - 1):
    n1[i+1] = n1calc(n1[i],n2[i],n3[i],n4[i],n5[i],n6[i],n7[i],t[i],h)
    n2[i+1] = n2calc(n1[i],n2[i],n3[i],n4[i],n5[i],n6[i],n7[i],h) 
    n3[i+1] = n3calc(n1[i],n2[i],n3[i],n4[i],n5[i],n6[i],n7[i],h) 
    n4[i+1] = n4calc(n1[i],n2[i],n3[i],n4[i],n5[i],n6[i],n7[i],h) 
    n5[i+1] = n5calc(n1[i],n2[i],n3[i],n4[i],n5[i],n6[i],n7[i],h) 
    n6[i+1] = n6calc(n1[i],n2[i],n3[i],n4[i],n5[i],n6[i],n7[i],h) 
    n7[i+1] = n7calc(n1[i],n2[i],n3[i],n4[i],n5[i],n6[i],n7[i],t[i],h) 
#graphing for each
plt.plot(t,n1-700)
plt.plot(t,n2-1000)
plt.plot(t,n3-36000)
plt.plot(t,n4-130)
plt.plot(t,n5-700)
plt.plot(t,n6-60)
plt.plot(t,n7-1500)
plt.legend(["Atmosphere","Mixed Upper Ocean","Deep Ocean","Small Biota","Large Biota","Detritus","Soil"])
plt.axis([0,80,0,100])
plt.xlabel('Time')
plt.ylabel('Change in mass (GT)')
plt.title('Change in Mass Over Time with Human Intervention')


plt.show()


