def rectangles(step):
	if step == 1:
		return 1
	else:
		count = 0
		for i in range(1 , step + 1):
			count += i**3

		return count

print(rectangles(1))
print(rectangles(2))
print(rectangles(3))