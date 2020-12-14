import random
from math import *

#----------- Number 1 -------------

def isPrime(n):
    if n > 1:
        # iterating from 2 to n / 2
        for i in range(2, n):

            # not prime if divisible
            if (n % i) == 0:
                return False
                break
        else:
            return True

    else:
        return False

def gcd(a, b):

    return a if b == 0 else gcd(b, a % b)

def RSA(size):

    p = random.randrange(20, 4000)
    q = random.randrange(20, 4000)
    prime = False

    while prime == False:
        p = random.randrange(size)
        prime = isPrime(p);
    prime = False

    while prime == False:
        q = random.randrange(size)
        prime = isPrime(q);

    n = p * q

    while True:
        e = random.randrange(size)
        if gcd(e, (p - 1) * (q - 1)) == 1:
            break

    return (e, n)


# ----------- Number 2 --------------

#n will be equal to 10,000
def SieveOfEratosthenes(n):

    #creating an array and if it is prime the value will be true and inside the array
    isPrime = [True for i in range(n + 1)]

    #making sure that P does not count 1 so we are starting at 2
    primeNums = 2
    while (primeNums * primeNums <= n):


        if (isPrime[primeNums] == True):

            # We are going to need to update all multiples of the "primeNumber" / number
            for i in range(primeNums * primeNums, n + 1, primeNums):

                isPrime[i] = False
         #if it is false were going to add 1 and loop again to check the next number
        primeNums += 1

    #now we have to do this loop to print all the prime numbers less than 10,000
    for primeNums in range(2, n + 1):
        if isPrime[primeNums]:
            print((primeNums), end=' ')



# ----------- Number 3 --------------

def primeFactorization(n):
    pfactors = []
    while n % 2 == 0:
        pfactors.append(2)
        n /= 2

    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            pfactors.append(int(i))
            n /= i

    if n > 2:
        pfactors.append(n)

    return pfactors


def findDivisors(start, div, array):
    # if we dont have any prime factors just end and return
    if start == len(array):
        print(div, end=' ')
        return

    #here we start to find the divisors
    for i in range(array[start][0] + 1):
        findDivisors(start + 1, div, array)
        div *= array[start][1]



def divisors(n):
    #create an array that stores prime factors
    holdDivisors = []
    #we can also just call prime factorization of n wich returns the array
    #of prime factors
    arr2 = primeFactorization(n)
    # or we can just find the prime factorization of n here as well
    i = 2
    while (i * i <= n):
        if (n % i == 0):
            count = 0
            while (n % i == 0):
                n //= i
                count += 1
            # we should count how many times we have that factor
            holdDivisors.append([count, i])
    if (n > 1):
        holdDivisors.append([1, n])
    start = 0
    div = 1
    findDivisors(start, div, holdDivisors)


#-------- Driver Program -------

if __name__ == '__main__':
    print("\nRSA: ")
    print(RSA(1000))
    print("\nPrime Factors:")
    print(primeFactorization(6))
    print("Divisors: ")
    print((divisors(6)))
    print("\nSieve of Eratosthenes:")
    print(SieveOfEratosthenes(10000))




