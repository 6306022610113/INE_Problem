def combinations(*items):       #รับค่าตัวแปรแบบอาร์กิวเมนต์
	product = 1                 #สร้างตัวแปร product ให้มีค่าเท่ากับ 1
	for i in items:             #ถ้า i มีค่าใน items
		if i:                   
			product *= i        #ให้ค่าใน product คูณกับ i
	return product              #ส่งค่า product ออกไป

print(combinations(2, 3))
print(combinations(3, 7, 4))
print(combinations(2, 3, 4, 5))