def find_the_difference(s, t):				# สร้างฟังก์ชั่นที่ รับค่าสตริงมา 2 ค่าเก็บไว้ใน s และ t จากนั้น
	for i in s:								# สร้างลูปขึ้นมาว่า ให้วนลูปเช็คในตัวแปล s จากนั้น สร้างเงื่อนไขว่า ถ้า
		if i in t:							# ตัวที่เช็คในลูปของ s ถ้ามีใน t เหมือนกันให้ แทนที่ ตัวที่มีเหมือนกันใน t เป็น spacebar
			t = t.replace(i,'',1)			# หรือ ว่างเปล่า นั่นเอง จากนั้น ตัวไหนก็ตามที่ใน s ไม่มี แต่ใน t มี ตัวนั้นจะเหลืออยู่
	return t								# ไม่โดนแทนที่ด้วย spacebar หรือว่างเปล่า จากนั้น รีเทิร์น ค่าทื่เหลืออยู่ใน t ออกมา

print(find_the_difference("abcd", "abcde"))	
print(find_the_difference("", "y"))			
print(find_the_difference("ae", "aea"))