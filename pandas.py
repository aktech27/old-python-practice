from numpy import *
from random import *
l=[]
for i in range(1,26):
    l.append(i)
shuffle(l)
l=array(l)
pcmatrix=l.reshape(5,5)
print(pcmatrix)
num=int(input())
r,c=where(pcmatrix==num)
pcmatrix[r,c]=0
print(pcmatrix)
zerom=zeros((5,5),dtype='int32')
print(zerom)
