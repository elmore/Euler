#!/usr/bin/env python3.6
import math

def SumOfFactorials(d):
    sd = 0
    for c in str(d):
        sd += math.factorial(int(c))
    return sd

def BuildChain(cache, startVal):
    curVal = startVal
    chain = []
    while curVal not in chain:
        chain.append(curVal)
        if curVal in cache:
            curVal = cache[curVal]
        else:
            nextVal = SumOfFactorials(curVal)
            cache[curVal] = nextVal
            curVal = nextVal
    return chain

chains = {}
sixtyInLengthCount = 0
for i in range(1, 1000000):
    thisChain = BuildChain(chains, i)
    if len(thisChain) == 60:
        sixtyInLengthCount += 1

print(sixtyInLengthCount)