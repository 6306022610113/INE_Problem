def car_timer(n):
	minutes = n%60
	hours = n // 60
	return (minutes%10) + (hours % 10) + minutes//10 + hours // 10

print(car_timer(240))
print(car_timer(808))
print(car_timer(14))