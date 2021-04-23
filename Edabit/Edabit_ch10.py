def combinations(*items):
	product = 1
	for item in items:
		if item:
			product *= item 
	return product

print(combinations(2, 3))
print(combinations(3, 7, 4))
print(combinations(2, 3, 4, 5))