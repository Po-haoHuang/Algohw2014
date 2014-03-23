# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 12:56:18 2014

@author: Po-hao Huang
"""
import sys
import random
sys.setrecursionlimit(2000)
def readin():
    temp = sys.stdin.readline()
    temp = temp.split()
    total = int(temp[0])
    n = int(temp[1])
    a=[]
    for i in range(0,total):
        a.append(sys.stdin.readline())
    a = map(float, a)
    result = randomselect(a,0,total-1,n)
    Output(result)
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
#    i = random.randint(p,r)
    while(True):
        i = random.randint(p,r)
        if i > ((9*p+r)/10) and i< ((p+9*r)/10):
            break
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
    A[r] = temp
    return i+1
def Output(result):
    print("{0:.15f}".format(result))

readin()