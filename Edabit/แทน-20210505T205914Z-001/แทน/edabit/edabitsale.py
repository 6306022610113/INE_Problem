def sock_merchant(lst):
	colors = {}
	for i in lst:
		if i not in colors:
			colors[i] = 1
		else:
			colors[i] += 1
	counts = [colors[i]//2 for i in colors]
	return sum(counts)

print(sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]))