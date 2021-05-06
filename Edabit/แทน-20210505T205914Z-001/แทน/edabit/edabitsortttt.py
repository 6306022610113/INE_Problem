def sort_array(lst):
	slst = []
	while True:
		slst.append(min(lst))
		lst.remove(min(lst))
		if lst == []:
			return slst

print(sort_array([2, -5, 1, 4, 7, 8]))