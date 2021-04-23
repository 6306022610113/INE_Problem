def shared_letters(a, b):               #รับค่าตัวเเปร a และ b
	lst = []                            #สร้างตัวแปรรับค่า     
	for i in a.lower():                 #ถ้า i มีค่าใน a เป็นตัวพิมพ์เล็ก
		if i in b.lower():              #และ i มีค่าน b 
			lst.append(i)               #ให้เพิ่ม i ในตัวแปร lst
	return ''.join(sorted(set(lst)))    #ส่งตัวข้อมูลใน lst ออก

print(shared_letters("house", "home"))
print(shared_letters("Micky", "mouse"))
print(shared_letters("house", "villa"))