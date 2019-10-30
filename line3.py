import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

A= np.array([0,4])
B= np.array([3,0])
len=10

x_AB= np.zeros((2,len))
lam= np.linspace(0,10,len)
for i in range(len):
	m= B-A
	temp= A + lam[i]*m
	x_AB[:,i]= temp.T

plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')	

plt.plot(A[0], A[1],'ro')
plt.text(A[0]*(1+0.1),A[1]*(1-0.1),'A')
plt.plot(B[0],B[1],'ro')
plt.text(B[0]*(1-0.1),B[1]*(1.1),'B')

C= np.array([0,3])
D= np.array([4,0])

x_CD= np.zeros((2,len))
lam= np.linspace(0,10,len)
for i in range(len):
	n= D-C
	temp= C + lam[i]*n
	x_CD[:,i]= temp.T

plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')	
plt.grid()

plt.plot(C[0], C[1],'ro')
plt.text(C[0]*(1+0.1),C[1]*(1-0.1),'C')
plt.plot(D[0],D[1],'ro')
plt.text(D[0]*(1-0.1),D[1]*(1.1),'D')
plt.axis([-2,6,-2,6])

plt.show()

n1= omat@m
n2= omat@n

p= np.zeros(2)
p[0]= n1.T@A
p[1]= n2.T@C

N= np.vstack((n1.T,n2.T))
H= np.linalg.inv(N)@p
print(H)
