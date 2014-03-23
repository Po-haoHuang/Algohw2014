# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 12:56:18 2014

@author: Po-hao Huang
"""
import sys
import random
sys.setrecursionlimit(2000)
def gen():
    print "digit,point digit,total number,number of smallest"
    temp = sys.stdin.readline().split()
    digit_num = int(temp[0])
    point_num = int(temp[1])
    total_num = int(temp[2])
    num_smallest = int(temp[3])
    a = []
    s = ""
    for i in range(0,total_num):
            s = ""
            s += str(random.randint(0,digit_num))
            s += '.'
            s += str(random.randint(0,point_num))
            a.append(float(s))
    b=a
    result = randomselect(a,0,total_num-1,num_smallest)
    b.sort()
    print ("{0:.15f}vs{0:.15f}".format(result,b[num_smallest-1]))


#def readin():
#    fo = open("test.txt", "r")
#    temp = fo.readline()
#    a = fo.readlines()
#    a = map(float, a)
#    temp = temp.split()
#    total = int(temp[0])
#    n = int(temp[1])
#    result = randomselect(a,0,total-1,n)
#    Output(result)
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
    i = random.randint(p,r)
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

gen()
