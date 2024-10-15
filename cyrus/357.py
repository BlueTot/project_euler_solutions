import numpy
import math

def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n//3 + (n%6==2), dtype=bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

def factors(n):
    for i in range(1,int(math.sqrt(n))+1):
        if n%i == 0:
            yield(i,n//i)

primelist = set(primesfrom2to(10**8))

total = 0
for i in range(10**8):
    print(i)
    for f, g in factors(i):
        if f+g not in primelist:
            break
    else:
        total += i
print(total)