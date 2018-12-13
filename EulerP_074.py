import numpy as np


fact_cache = {}

def factorial(n):
	if n == 0:
		return 1
	elif n == 1:
		return 1
	elif n in fact_cache:
		return fact_cache[n]
	else:
		fact = factorial(n-1) * n
		fact_cache[n] = fact
		return fact

fact_sum_cache = {}

def fact_sum(nums):
	print (nums)
	nums = tuple(sorted(int(x) for x in str(nums)))
	if nums in fact_sum_cache:
		return fact_sum_cache[nums]
	elif nums[:-1] in fact_sum_cache:
		return fact_sum(fact_sum_cache[nums[:-1]] + nums[-1])
	else:
		Sum = 0
		for n in nums:
			Sum += factorial(n)

		fact_sum_cache[tuple(sorted(nums))] = Sum
	return Sum


loop_cache = {}

a = 69
# for j in range(69,70):
for j in [69,78,169]:
	starting_val = j
	loop = []
	for i in range(5):
		j = fact_sum(j)
		if j in loop:
			loop.append(j)
			loop = [starting_val] + loop
			print (loop[-1] in loop[:-1])
			print (loop)
			index = np.ravel(np.where(np.array(loop[:-1]) == np.array(loop[-1])))[0]
			print (loop[:-1] == loop[-1])
			print (5-index)
			print (loop[index:-1])
			for item in loop[index:-1]:
				loop_cache[item] = 5-index
			print ('fin')
			break	
		loop.append(j)
	loop = [starting_val] +  loop
	print (loop[-1] in loop[:-1])
	print (loop)
	print (len(loop))
	print (starting_val)
print (loop_cache)
