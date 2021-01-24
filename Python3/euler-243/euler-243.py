#!/usr/bin/env python3.6

# is f1 less than f2
def IsLessThan(f1, f2):
    m = f2[1] / f1[1]
    return f1[0]*m < f2[0]

def IsResiliant(n,d):
    for i in range(2, n+1):
        if n % i == 0 and d % i == 0:
            return False
    return True

def CountResliant(d):
    return sum(IsResiliant(i, d) for i in range(1, d))


#target = (15499, 94744)
target = (4, 10)

lt = False
d = 1
while not lt:
    d += 1
    c = CountResliant(d)
    resiliance = (c, d-1)
    lt = IsLessThan(resiliance, target)
    print(f'{resiliance} : {lt}')
    if lt:
        print(f'smallest denominator is {d}')
    

 