import numpy as np
import matplotlib.pyplot as plt
from coeffs import*

omat1= np.array([0,-1])
omat2= np.array([1,0])
omat= np.vstack((omat1,omat2))

p= np.zeros(2)
O= np.array([0,0])

n1= np.array([1,1])
p[0]= 2

n2= omat@n1
p[1]= 0

N= np.vstack((n1,n2))
F= np.linalg.inv(N)@p

d= np.linalg.norm(O-F)
s= 2*np.sqrt(3)*d

area= 0.5*3*d*s
print("Area = ",area)

A= F+ n2*s*0.5/np.linalg.norm(n2)
B= F- n2*s*0.5/np.linalg.norm(n2)
C= -(A+B)

print(A)
print(B)
print(C)

x_AB= line_gen(A,B)
x_BC= line_gen(B,C)
x_CA= line_gen(C,A)

plt.plot(x_AB[0,:], x_AB[1,:], label='$AB$')
plt.plot(x_BC[0,:], x_BC[1,:], label='$BC$')
plt.plot(x_CA[0,:], x_CA[1,:], label='$CA$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1+0.1), A[1]*(1-0.1), 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1-0.2), B[1]*(1), 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1+0.005), C[1]*(1-0.1), 'C')

D= (B+C)/2
E= (A+C)/2
F= (A+B)/2

x_AD= line_gen(A,D)
x_BE= line_gen(B,E)
x_CF= line_gen(C,F)

plt.plot(x_AD[0,:], x_AD[1,:], label='$AD$')
plt.plot(x_BE[0,:], x_BE[1,:], label='$BE$')
plt.plot(x_CF[0,:], x_CF[1,:], label='$CF$')

plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1+0.1), D[1]*(1-0.1),'D')
plt.plot(E[0], E[1], 'o')
plt.text(E[0] * (1-0.2), E[1]*(1), 'E')
plt.plot(F[0], F[1], 'o')
plt.text(F[0] * (1+0.005),F[1]*(1-0.1), 'F')
plt.plot(O[0], O[1], 'o')
plt.text(O[0] * (1+0.1), O[1]*(1-0.1),'O')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()

plt.show()
