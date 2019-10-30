import numpy as np
import matplotlib.pyplot as plt
from coeffs import*

A= np.array([0,0])
B= np.array([0,2])
D= np.array([2,0])
C= np.array([2,2])
theta= np.pi/6


p= A+B+C+D

T= np.array(([np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]))

multi= np.array([1,0])

sum= multi@T@p
print(sum)

L= T@A
M= T@B
N= T@C
O= T@D

x_AB= line_gen(A,B)
x_BC= line_gen(B,C)
x_CD= line_gen(C,D)
x_DA= line_gen(D,A)

plt.plot(x_AB[0,:], x_AB[1,:], label='$AB$')
plt.plot(x_BC[0,:], x_BC[1,:], label='$BC$')
plt.plot(x_CD[0,:], x_CD[1,:], label='$CD$')
plt.plot(x_DA[0,:], x_DA[1,:], label='$DA$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1+0.1), A[1]*(1-0.1), 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1-0.2), B[1]*(1), 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1+0.005), C[1]*(1-0.1), 'C')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1+0.1), D[1]*(1-0.1), 'D')

x_LM= line_gen(L,M)
x_MN= line_gen(M,N)
x_NO= line_gen(N,O)
x_OL= line_gen(O,L)

plt.plot(x_LM[0,:], x_LM[1,:], label='$LM$')
plt.plot(x_MN[0,:], x_MN[1,:], label='$MN$')
plt.plot(x_NO[0,:], x_NO[1,:], label='$NO$')
plt.plot(x_OL[0,:], x_OL[1,:], label='$OL$')

plt.plot(M[0], M[1], 'o')
plt.text(M[0] * (1-0.2), M[1]*(1), 'M')
plt.plot(N[0], N[1], 'o')
plt.text(N[0] * (1+0.005), N[1]*(1-0.03), 'N')
plt.plot(O[0], O[1], 'o')
plt.text(O[0] * (1+0.03), O[1]*(1-0.1), 'O')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.axis('equal')
plt.grid()

plt.show()



