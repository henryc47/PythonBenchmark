import time
import sys
import math

#generate all primes up to n
def generateNPrimes(n : int):
    primes = []
    for i in range(2,n):
        primes = checkPrime(i,primes)

def checkPrime(i,primes):
    is_prime = True
    max_i = math.ceil(math.sqrt(i))
    for prime in primes:
        if prime>max_i:
            break
        if i%prime==0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
    return primes
        

if __name__ == "__main__":
    t1 = time.time()
    generateNPrimes(int(sys.argv[1]))
    t2 = time.time()
    print("execution time =",t2-t1,"seconds")

