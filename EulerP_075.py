import numpy as np

triangles = {}
nums = np.arange(1,100)
for i in nums:
	for j in nums[i:]:
		val = (i**2+j**2)**.5
		if val == int(val):
			nums = np.delete(nums, np.where(nums==val))
			perimeter = int(i + j + val)
			if perimeter in triangles:
				triangles[perimeter] += 1
			else:
				triangles[perimeter] = 1

print (triangles[12])
print (triangles.items())
print (np.array(list(triangles.items())))
