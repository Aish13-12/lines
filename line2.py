import numpy as np
import matplotlib.pyplot as plt

A= np.array([4,0])
B= np.array([0,-4])
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
plt.text(B[0]*(1+0.1), B[1]*(1+0.1), 'B')

P= np.array([2,1])
h= np.array([1,1])

Q= P - np.sqrt(6)*h
print(Q)

len= 10

x_PQ= np.zeros((2,len))

lam= np.linspace(0,1,len)
for i in range(len):
	m= Q-P
	temp1= P + lam[i]*m
	x_PQ[:,i]= temp1.T

plt.plot(x_PQ[0,:], x_PQ[1,:], label='$PQ$')


plt.plot(P[0], P[1], 'ro')
plt.text(P[0]*(1+0.03), P[1]*(1-0.1), 'P')
plt.plot(Q[0],Q[1], 'ro')
plt.text(Q[0]*(1+0.1), Q[1]*(1+0.1), 'Q')

plt.grid()
plt.show()
