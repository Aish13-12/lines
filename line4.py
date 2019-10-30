import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

W= np.array([0,1])
X= np.array([-1,0])
len=10

x_WX= np.zeros((2,len))
lam= np.linspace(0,10,len)
for i in range(len):
	m= X-W
	temp= W + lam[i]*m
	x_WX[:,i]= temp.T

plt.plot(x_WX[0,:],x_WX[1,:],label='$WX$')

plt.plot(W[0], W[1],'ro')
plt.text(W[0]*(1+0.1),W[1]*(1-0.1),'W')
plt.plot(X[0],X[1],'ro')
plt.text(X[0]*(1-0.1),X[1]*(1.1),'X')

Y= np.array([0,-5])
Z= np.array([5/7,0])

x_YZ= np.zeros((2,len))
lam= np.linspace(0,10,len)
for i in range(len):
	n= Z-Y
	temp= Y + lam[i]*n
	x_YZ[:,i]= temp.T

#plt.plot(x_YZ[0,:],x_YZ[1,:],label='$YZ$')

#plt.plot(Y[0], Y[1],'ro')
#plt.text(Y[0]*(1+0.1),Y[1]*(1-0.1),'Y')
#plt.plot(Z[0],Z[1],'ro')
#plt.text(Z[0]*(1-0.1),Z[1]*(1.1),'Z')
#plt.axis([-3,4,-7,5])

#plt.show()

n1= omat@m
n2= omat@n

p= np.zeros(2)
p[0]= n1.T@W
p[1]= n2.T@Y

N= np.vstack((n1.T,n2.T))
A= np.linalg.inv(N)@p

P= np.array([-1,-2])
d= np.linalg.norm(A-P)
M= A-P
#print(M)

C= P- d*(M/np.linalg.norm(M))

N= omat@M/2
print(N)

B= P- d*(N/np.linalg.norm(N))
D= P+ d*(N/np.linalg.norm(N))

print("A = ",A)
print("B = ",B)
print("C = ",C)
print("D = ",D)

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

x_BC= np.zeros((2,len))
lam= np.linspace(0,10,len)
for i in range(len):
	m= C-B
	temp= B + lam[i]*m
	x_BC[:,i]= temp.T

plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')

x_DA= np.zeros((2,len))
lam= np.linspace(0,10,len)
for i in range(len):
	n= A-D
	temp= D + lam[i]*n
	x_DA[:,i]= temp.T

plt.plot(x_DA[0,:],x_DA[1,:],label='$DA$')	

plt.axis([-8,6,-10,6])
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')

plt.show()
