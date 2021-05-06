def seq_level(lst):														# สร้างฟังก์ชั่นขึ้นมารับค่า จากนั้นสร้างเงื่อนไข
	if lst[1]-lst[0] == lst[2]-lst[1]:									# ถ้า index ที่สองลบกับ index แรก แล้วเท่ากับ index
		return "Linear"													# ที่สามลบกับ index ที่สอง ให้รีเทิร์น Linear(เชิงเส้น)ออกมา
	elif lst[3] - (2*lst[2]) + lst[1] == lst[2] - (2*lst[1]) + lst[0]:	# ถ้า index ที่สี่ลบกับ (สองที่คูณกับ index ที่ สาม)บวก แล้ว
		return "Quadratic"												# บวกกับ index ที่สอง เท่ากับ index ที่สามลบกับ
	else:																# (สองที่คูณกับ index ที่สอง) แล้วบวกกับ index แรก
		return "Cubic"													# ให้รีเทิร์นค่า Quadratic ออกมา
																		# แต่ถ้าไม่ใช่ ทั้งสองเงื่อนไขข้างต้น ให้รีเทิร์น Cubic
print(seq_level(1, 2, 3, 4, 5))
print(seq_level(3, 6, 10, 15, 21))
print(seq_level(4, 14, 40, 88, 164))