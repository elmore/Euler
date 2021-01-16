#!/usr/bin/env python3.6
import math
from algo import Run
#from draw import Draw

# def RunIter(number):
#     (colours, _, _) = Run(number)
#     blackCount = sum(colours[c] == "black" for c in colours)
#     print(f'{number}, {blackCount}')
#     Draw(colours, '/home/tom/Workspace/Euler/walk.bmp')
#     return blackCount

# dy = RunIter(11000)



# by 'long-term-behaviour' and 'find-repitiion-length' we know after ~10k the pattern 
# starts repeating with a period of 104 and that the number of black squares increases 
# by 12 each period.

# the value at 10^18 will be a multiple of 12 more than any iteration after 10k which is 
# at the same point in the repeating pattern.

# print(math.floor((pow(10, 18) - pow(10, 4)) / 12))
# print(math.ceil((pow(10, 18) - pow(10, 4)) / 12))

# print((pow(10, 18) - pow(10, 4)) / 12)
# # 0
# print((pow(10, 18) - pow(10, 4)) % 12)

# 9615384615384520




def CalcCount(targetNumber, lowNumberInLinearRegion):
    print(f'Using {lowNumberInLinearRegion}')

    print(f'Remainder = {(targetNumber - lowNumberInLinearRegion) % 104}')

    multiple = (targetNumber - lowNumberInLinearRegion) / 104

    (colours, _, _) = Run(lowNumberInLinearRegion)
    lowCount = sum(colours[c] == "black" for c in colours)

    countAt10ToEighteen = lowCount + multiple * 12

    print(int(countAt10ToEighteen))






targetNumber = pow(10, 18)
lowNumberInLinearRegion = 20000

for i in range(20000, 21000):
    remainder = (targetNumber - i) % 104
    if remainder == 0:
        lowNumberInLinearRegion = i
        CalcCount(targetNumber, lowNumberInLinearRegion)

# CalcCount(targetNumber,lowNumberInLinearRegion )

#lowNumberInLinearRegion = 30004

# print(f'Using {lowNumberInLinearRegion}')

# print(f'Remainder = {(targetNumber - lowNumberInLinearRegion) % 104}')

# multiple = (targetNumber - lowNumberInLinearRegion) / 104

# (colours, _, _) = Run(lowNumberInLinearRegion)
# lowCount = sum(colours[c] == "black" for c in colours)

# countAt10ToEighteen = lowCount + multiple * 12

# print(int(countAt10ToEighteen))

# 115384615384614928