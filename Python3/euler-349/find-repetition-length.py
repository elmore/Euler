#!/usr/bin/env python3.6
from algo import Run

(_, _, directions) = Run(20000)

# starts repeating after ~10000
# wherever we start after 11k will 
# eventually start to repeat

startIndex = 11000
endPointer = 0
startPointer = 0
# start with 1 offset so pointer doesnt immediately match
for i in range(startIndex+1, 20000):
    # if the end pointer has started counting, begin the start pointer.
    # once the end pointer stops being reset it will continue incrementing and then once 
    # the start pointer also stops being reset then they will stay in lock step with each     
    # other, with the difference in index being the repeating period.
    if(endPointer > 0):
        # repeat the same 
        if directions[i] == directions[startPointer + startIndex]:
            startPointer += 1
        else: 
            startPointer = 0
    if directions[i] == directions[endPointer + startIndex]:
        endPointer += 1
    else:
        endPointer = 0
        startPointer = 0

# 104
period = endPointer - startPointer
print(f'Pattern repeats every {period} iterations')


(c20000, _, _) = Run(20000)
blackCountAt20000 = sum(c20000[c] == "black" for c in c20000)

(c20kPlusPeriod, _, _) = Run(20000 + period)
blackCountAtc20kPlusPeriod = sum(c20kPlusPeriod[c] == "black" for c in c20kPlusPeriod)

# 12
diffBlackCount = blackCountAtc20kPlusPeriod - blackCountAt20000
print(f'Every {period} iterations the black count increases by {diffBlackCount}')

