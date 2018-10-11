###Calculating Work Function,frequency, Kinetic Energy & Graph b/w K.E & wavelength###
#######################################################################################
#######################################################################################


import matplotlib.pyplot as plt

# H constant define
h = 6.626 * 10**-34

#Threshold frequency define
tf = 4

#Speed of light define
c = 3 * 10**8

#definig Wavelength
L =[]
num = int(input('Enter the Number of Inputs for graph plotting: '))
for i in range(0,num):
    elem = float(input('Enter the values of wavelenght: '))
    L.append(elem)

#bubble sorting of Wavelenghth
for i in range(0,num):
    for j in range(i+1,num):
        if L[i]>L[j]:
            temp = L[i]
            L[i] = L[j]
            L[j] = temp

#defining Frequency
Feq = []
for i in range(0,num):
    div = c / L[i]
    Feq.append(div)

print("Frequency =",*Feq, sep = ", ")

#defining Kenetic Energy
Ke = []
for i in range(0,num):
    fur = h * ( Feq[i] - tf)
    Ke.append(fur)

print("Kinetic Energy =",*Ke, sep = ", ")

plt.plot(L,Ke, 'r-')
plt.xlabel('Wavelength')
plt.ylabel('Kinetic Energy')
plt.title('Graph between Wavelength and Kinetic Energy')
plt.show()


########################################################################################
########################################################################################
