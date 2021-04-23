def format_ascii(s, width):     #รับค่าตัวแปร ascii และความกว้าง
	s_new = []                  #สร้างตัวแปรรับค่า
	while s:                    #
		new = s[:width]         #ให้ตัวแปร ascii เท่ากับความกว้าง
		s_new.append(new)       #ให้เพิ่มค่า new เข้าไปใน s_new
		s = s[width:]           #ตัวแปร ascii เท่ากับความกว้าง

	s_new1 = '\n'.join(s_new)   #สร้างตัวแปรมารับค่าขึ้นบรรทัดใหม่ของ s_new
	return(s_new1)              #ส่งค่า s_new1 ออก

print(format_ascii("0123456789", 2))
print(format_ascii("................................", 8))
print(format_ascii("^^^^^^^^", 1))