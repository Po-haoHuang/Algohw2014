# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 12:56:18 2014

@author: Po-hao Huang
"""
import sys
import random
def readin():
    temp = sys.stdin.readline()
    a = sys.stdin.readlines()
    a = map(float, a)
    temp = temp.split()
    total = int(temp[0])
    n = int(temp[1])
    randomselect(a,0,total-1,n)

def randomselect(A,p,r,i):
    if p==r:
        return A[p]
    q = randompartition(A,p,r)
    k = q-p+1;
    if i==k:
        return A[q]
    elif i<k:
        return randomselect(A,p,q-1,i)
    else:
        return randomselect(A,q+1,r,i-k)
def randompartition(A,p,r):
    i = random.randint(p,r+1)
    temp = A[r]
    A[r] = A[i]
    A[i] = temp
    return partition(A,p,r)

def partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i = i+1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
    temp = A[i+1]
    A[i+1] = A[r]
    A[r] = A[i+1]
    return i+1



def Output(result):
    print("{0:.15f}".format(result))



readin()