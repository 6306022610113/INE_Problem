def rectangles(step):                   #รับค่าตัวแปร
	if step == 1:                       #ค่าที่รับมาเท่ากับ 1
		return 1                        #ส่งค่า 1 ออก
	else:
		count = 0                       #หรือ ให้ count คือ 0
		for i in range(1 , step + 1):   #ให้ i เท่ากับ 1 และให้ค่าสุดท้ายเป็น step + 1
			count += i**3               #ตัวแปร count เพิ่มค่า i กำลัง 3

		return count                    #ส่งค่า count

print(rectangles(1))
print(rectangles(2))
print(rectangles(3))