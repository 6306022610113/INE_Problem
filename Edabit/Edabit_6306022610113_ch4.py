def duplicate_nums(nums):           #รับค่า nums เข้าฟังก์ชัน
	n1 = []                         #สร้างตัวแปร n1, n2
	n2 = []
	
	for i in nums:                  #ถ้า i มีค่าใน nums
		if i not in n1:             #ถ้า i ไม่มีใน n1
			n1.append(i)            #ให้เพิ่มเข้าไปให้ตัวแปร n1
		else:
			n2.append(i)            #หรือถ้ามีการใน n1 แล้ว ให้เอาไปไว้ใน n2 แทน
			
	return sorted(n2) or None       #ถ้ามีค่าใน n2 เรียงค่าน้อยไปมาก 
                                    #หรือถ้าไม่มีให้ส่งค่า None ออกไปแทน
print(duplicate_nums([1, 2, 3, 4, 3, 5, 6]))
print(duplicate_nums([81, 72, 43, 72, 81, 99, 99, 100, 12, 54]))
print(duplicate_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))