#!/usr/bin/env python3.6


# for fractions where num and den have 2 digits and share at least one of those digits
#     for each way to cancel one digit
#         perform cancelation
#         check equivalence

def combine(a,b):
    return int(f'{a}{b}')

def commonDigits(n1,n2,d1,d2):
    n = combine(n1, n2)
    d = combine(d1, d2)
    if n > d : return False
    return n1 == d1 or n1 == d2 or n2 == d1 or n2 == d2

def equivalent(n1, d1, n2, d2):
    return n1/d1 == n2/d2

def permutations(n1,n2,d1,d2):
    perms = []
    if n1 == d1 and n2 == d2 : return perms
    if n1 == d1 : perms.append((n2,d2))
    if n1 == d2 : perms.append((n2,d1))
    if n2 == d1 : perms.append((n1,d2))
    if n2 == d2 : perms.append((n1,d1))
    return perms

for num_a in range(1, 10):
    for num_b in range(1, 10):
        for den_a in range(1, 10):
            for den_b in range(1, 10):
                if commonDigits(num_a, num_b, den_a, den_b):
                    for p in permutations(num_a,num_b,den_a,den_b):
                        if equivalent(combine(num_a,num_b),combine(den_a,den_b),p[0],p[1]):
                            print(f'{num_a}{num_b}/{den_a}{den_b}')
