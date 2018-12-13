import numpy as np

def sievePrimes(n):
	sieve = np.ones(n, dtype=bool)
	sieve[:2] = False
	sieve[::2] = False
	num = 3	
	
	while num < n:
		sieve[slice(2*num,n,num)] = False	
		num += 2

	return np.concatenate(([2], np.arange(n)[sieve]), axis=0), sieve

if __name__ == '__main__':
	n = 10000
	primes, sieve = sievePrimes(n)

	odds = np.ones(n, dtype=bool)
	odds[::2] = False
	odds_composite = np.arange(n)[odds & ~sieve]

	squares_times_2 = (2*(np.arange(n/2)**2)).astype(int)
	potential = np.add.outer(primes, squares_times_2)
	potential = potential[potential < n]
	potential = np.array(list(set(potential)))
	potential = np.sort(potential)
	potential = potential[potential % 2 != 0]
	print (odds_composite)
	print (potential[potential < n])
	soln = odds_composite[np.isin(odds_composite, potential,invert=True)]
	print (soln)
