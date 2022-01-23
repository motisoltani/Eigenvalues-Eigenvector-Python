'''
Eigenvalues & Eigenvector 
language: Python

Motahare Soltani
soltani.wse@gmail.com

'''

import numpy as np
from numpy import linalg as LA

A=np.array([[1,2,3],[3,2,1],[1,0,-1]])
w,v=LA.eig(A)
print(w)
print(v)
