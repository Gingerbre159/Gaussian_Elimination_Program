
# coding: utf-8

# Thomas Carter <br>
# 10/9/20

# In this file is a function that solves the matrix equation Ax = b using Gaussian Elimination. This function will accept as input an n-by-n matrix A and an n-by-1 vector b, and it should produce a n-by-1 vector x that satisfies Ax = b.


# Imports

import random


# Functions

def swap(a, b):
    temp = b
    b = a
    a = temp
    
    return a, b


def GaussianElimination(A, b, n):
    x = []
    
    if n <= 0:
        return x
    
    # Forward Elimination, impliments pivoting
    for i in range(0,n-1): 
        pivotrow = i
        for j in range(i+1,n):
            if abs(A[j][i]) > abs(A[pivotrow][i]):
                pivotrow = j
        for j in range(i, n):
            swap(A[i][j], A[pivotrow][j])
        for j in range(i+1, n):
            temp = A[j][i]/A[i][i]
            for k in range(i,n):
                A[j][k] = A[j][k] - A[i][k] * temp
    
    
    for i in range(0,n): #to make x the length of n and full of zeros
        x.append(0)
    
    
    # Back Substitution
    x[n-1] = b[n-1]/A[n-1][n-1] 
    for i in range(n-2, -1, -1): #i is counting down from the second to last x value to the first
        s = 0 #sum
        for j in range(i+1, n): 
            s = s + A[i][j]*x[j] #sum of knowns
        x[i] = (b[i] - s)/A[i][i] #new x value
    
    
    return x


# Main

print("Please input the size of the matrix (the format is positive whole numbers only): ")
n = int(input())
print("")


# The matrix
A = []
for j in range(n):
    tempList = []
    for i in range(n):
        num = random.randint(-9,9)
        while num == 0: #this is to ensure that we never divide by 0
            num = random.randint(-9,9)
        tempList.append(num)
    A.append(tempList)
    
print('A:')
for i in range(0,n):
    print(A[i])

print('')


# The vector
b = [] 
for k in range(n):
    num = random.randint(-9,9)
    b.append(num)

print('b:')
print(b)

print('')


# The solution (AKA: x)
print('x:')
x = GaussianElimination(A,b,n)
print(x)

print('')


# This checks to make sure everything worked
if n > 0:
    checker = 0
    for i in range(0,n):
        checker = checker + A[0][i]*x[i]
    if checker >= (b[0]-0.1) and checker <= (b[0]+0.1): #to account for rounding error
        print('It works! :D')
    else:
        print('It did not work :(')
else:
    print("Please only use positive whole numbers.")

