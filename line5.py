import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

a= 5
b= 13
c= -46
k1= (-b + np.sqrt(b*b-(4*a*c)))/(2*a)
k2= (-b - np.sqrt(b*b-(4*a*c)))/(2*a)

print("k1 = ", k1)
print("k2 = ",k2)

A= np.array([k1,-3*k1])
B= np.array([5,k1])
C= np.array([-k1,2])

#print (A)
#print (B)
#print (C)

p= np.zeros(2)

n1= dir_vec(B,C)
p[0]= n1@A

n2= dir_vec(C,A)
p[1]= n2@B

N= np.vstack((n1,n2))
H= np.linalg.inv(N)@p
print("Orthocentre = ", H)
