def normal_sequence(n):
	return [0, 1, 1, 2, 0, 2, 2, 1][(n - 1) % 8]

print(normal_sequence(0)) 

print(normal_sequence(1)) 

print(normal_sequence(8))


print(normal_sequence(10))