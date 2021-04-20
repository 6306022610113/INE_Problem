def happy_year(y):
	while True:
		y += 1
		if len(set(str(y))) == 4:
			return y

print(happy_year(2017))
print(happy_year(1990))
print(happy_year(2021))

