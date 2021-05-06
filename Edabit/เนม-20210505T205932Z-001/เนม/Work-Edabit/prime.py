def prime_in_range(n1, n2):
	if n2 == 2:
		return True
	for x in range(n1, n2 + 1):
		count = 0
		for y in range(2, x):
			if not x % y:
				count += 1
		if count == 0:
			return True
	return False

print(prime_in_range(15, 15))


print(prime_in_range(70, 30)) 


print(prime_in_range(35, 53))