import numpy as np
import matplotlib.pyplot as plt

A= np.array([2.5,0])
B= np.array([0, 10/3])
len= 10

x_AB= np.zeros((2,len))

lam= np.linspace(0,1,len)
for i in range(len):
	m= B-A
	temp1= A + lam[i]*m
	x_AB[:,i]= temp1.T

plt.plot(x_AB[0,:], x_AB[1,:], label='$AB$')


plt.plot(A[0], A[1], 'ro')
plt.text(A[0]*(1+0.03), A[1]*(1-0.1), 'A')
plt.plot(B[0],B[1], 'ro')
plt.text(B[0]*(1+0.1), B[1]*(1), 'B')

C= np.array([-5/8,0])
D= np.array([0,-5/6])
len= 10

x_CD= np.zeros((2,len))

lam= np.linspace(0,1,len)
for i in range(len):
	m= D-C
	temp1= C + lam[i]*m
	x_CD[:,i]= temp1.T

plt.plot(x_CD[0,:], x_CD[1,:], label='$CD$')


plt.plot(C[0], C[1], 'ro')
plt.text(C[0]*(1+0.1), C[1]*(1-0.1), 'C')
plt.plot(D[0],D[1], 'ro')
plt.text(D[0]*(1), D[1]*(1), 'D')

plt.grid()
plt.show()


