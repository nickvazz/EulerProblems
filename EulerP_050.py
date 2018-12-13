import numpy as np
import time

start = time.time()
  
def sievePrimes(n):
    sieve = np.ones(n, dtype=bool)
    sieve[:2] = False
    sieve[::2] = False
    num = 3

    while num < n:
        sieve[slice(2*num,n,num)] = False
        num += 2

    return np.concatenate(([2], np.arange(n)[sieve]), axis=0), sieve



def main():
	potentials = []
	n = 100000
	primes, sieve = sievePrimes(n)
	counter = 0
	print ('{} primes finished'.format(len(primes)))
	print (primes[-20:])
	for i in range(len(primes)):
		# print (i)
		if i == 0:
			start = 2
		if i > 0:
			start = 1
		for j in range(i+start,len(primes)+1, 2):
			if j - i == 1:
				continue
			counter += 1
			Sum = np.sum(primes[i:j])
			if Sum > n:
				break
			if Sum in primes:
				potentials.append((Sum, j-i))

	print (counter)
	print (sorted(potentials, key=lambda x: x[1], reverse=True)[:5])

if __name__ == '__main__':
	start = time.time()
	main()
	end = time.time()
	print (end - start)
