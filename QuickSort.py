import time
import random
import sys
sys.setrecursionlimit(10000000)
def QuickSort(A,s,e):
    if(s<e):
        p=Partition(A,s,e)
        QuickSort(A,s,p-1)
        QuickSort(A,p+1,e)
def Partition(A,s,e):
    pivot=A[e]
    j=s
    i=s-1
    for j in range(s,e):
        if A[j]<pivot:
            i+=1
            A[j],A[i]=A[i],A[j]
    A[i+1],A[e]=A[e],A[i+1]
    return i+1

n=int(input("Enter the number of test Cases:"))

SCase=[]
RCase=[]
NCase=[]
for i in range(n):
    s=int(input())
    arr=[]
    for j in range(s):
        arr.append(random.randrange(100))
    #UnsortedArray
    st=time.time()
    QuickSort(arr,0,s-1)
    ed=time.time()
    NCase.append(ed-st)
    #SortedArray
    st=time.time()
    QuickSort(arr,0,s-1)
    ed=time.time()
    SCase.append(ed-st)
    #ReverseSortedArray
    arr.reverse()
    st=time.time()
    QuickSort(arr,0,s-1)
    ed=time.time()
    RCase.append(ed-st)
print("\n\nSorted Case: ",SCase)
print("\n\nNormal Case: ",NCase)
print("\n\nReverSorted Case: ",RCase)