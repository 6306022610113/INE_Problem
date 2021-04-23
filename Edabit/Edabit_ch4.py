def duplicate_nums(nums):
	n1 = []
	n2 = []
	
	for i in nums:
		if i not in n1:
			n1.append(i)
		else:
			n2.append(i)
			
	return sorted(n2) or None

print(duplicate_nums([1, 2, 3, 4, 3, 5, 6]))
print(duplicate_nums([81, 72, 43, 72, 81, 99, 99, 100, 12, 54]))
print(duplicate_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))