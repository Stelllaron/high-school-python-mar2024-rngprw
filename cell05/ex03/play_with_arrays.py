#!/usr/bin/env python3

array =[2,8,9,48,8,22,-12,2]
nset = set()

print(array)

for i in range(0,len(array)):
    if int(array[i])>5:
        array[i]+=2
        nset.add(array[i])

print(nset)

