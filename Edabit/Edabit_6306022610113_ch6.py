def to_snake_case(txt):             #รับค่าตัวแปร txt
	r = ""                          #ตัวแปรรับค่า
	for a in txt:                   #ถ้า a มีใน txt
		if a.isupper():             #ถ้า a เป็นตัวพิมพ์ใหญ่
			r += "_"+a.lower()      #ให้ r เพิ่ม "_" และทำให้ a เป็นตัวพิมพ์เล็ก
		else:                   
			r += a                  # หรือ เพิ่ม a เข้าไปให้ตัวแปร r
	return r                        #ส่งค่า r ออกไป
	
def to_camel_case(txt):             
	r = ""                          
	u = False                       #กำหนด u ให้เป็น false
	for a in txt:                   
		if a == "_":                #ถ้า a เท่ากับ/มี "_"
			u = True                #ให้ u เป็น True
		elif u:                     
			r += a.upper()          #หรือ เพิ่ม a ตัวพิมพ์ใหญ่เข้าไปใน r
			u = False               #ให้ u เป็น false
		else:
			r += a                  
	return r                        #ส่งค่า r ออกไป

print(to_camel_case("hello_edabit"))
print(to_snake_case("helloEdabit"))
print(to_camel_case("is_modal_open"))
print(to_snake_case("getColor"))