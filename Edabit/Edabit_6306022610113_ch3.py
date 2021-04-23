def happy_year(y):					#รับค่า y เข้าฟังก์ชัน
	while True:						#ถ้าเป็นจริง
		y += 1						#ให้เอา y + 1
		if len(set(str(y))) == 4:	#ถ้าเก็บข้อมูลของข้อมูล y เท่ากับ 4
			return y				#ให้ส่งค่า y ออก

print(happy_year(2017))
print(happy_year(1990))
print(happy_year(2021))

