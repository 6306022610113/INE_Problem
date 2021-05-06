def antipodes_average(lst):
	return [0.5 * (lst[i] + lst[-(i+1)]) for i in range(len(lst)//2)]

print(antipodes_average([1, 5, 0, 4]))


print(antipodes_average([1, 4, 3, 2, 5]))


print(antipodes_average([-5, -3]))