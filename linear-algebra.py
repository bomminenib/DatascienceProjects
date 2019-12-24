# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 18:51:19 2019

@author: bomvenka1
"""

# # multiply vectors
# from numpy import array

# a = array([1, 2, 3])
# print(a)

# b = array([1, 2, 3])
# print(b)

# c = a * b
# print(c)



# # add matrices
# from numpy import array
# A = array([[1, 2, 3], [4, 5, 6]])
# print(A)
# B = array([[1, 2, 3], [4, 5, 6]])
# print(B)
# C = A + B
# print(C)



# # matrix dot product
# from numpy import array
# A = array([[1, 2], [3, 4], [5, 6]])
# print(A)
# B = array([[1, 2], [3, 4]])
# print(B)
# C = A.dot(B)
# print(C)



# # invert matrix
# from numpy import array
# from numpy.linalg import inv
# # define matrix
# A = array([[1.0, 2.0], [3.0, 4.0]])
# print(A)
# # invert matrix
# B = inv(A)
# print(B)



# # LU decomposition
# from numpy import array
# from scipy.linalg import lu
# # define a square matrix
# A = array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(A)
# # LU decomposition
# P, L, U = lu(A)
# print(P)
# print(L)
# print(U)
# # reconstruct
# B = P.dot(L).dot(U)
# print(B)



from numpy import array
from numpy import mean
from numpy import cov
from numpy.linalg import eig
# define a matrix
A = array([[1, 2], [3, 4], [5, 6]])
print(A)
# calculate the mean of each column
M = mean(A.T, axis=1)
print(M)
# center columns by subtracting column means
C = A - M
print(C)
# calculate covariance matrix of centered matrix
V = cov(C.T)
print(V)
# eigendecomposition of covariance matrix
values, vectors = eig(V)
print(vectors)
print(values)
# project data
P = vectors.T.dot(C.T)
print(P.T)