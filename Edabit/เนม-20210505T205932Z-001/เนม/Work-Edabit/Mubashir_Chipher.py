def mubashir_cipher(message):
	key= [['m', 'c'], ['u', 'e'], ['b', 'g'], ['a', 'k'], ['s', 'v'], ['h', 'x'], #กำหนดlistชื่อkeyที่มีคู่ลำดับตามที่โจทย์กำหนด
    ['i', 'z'], ['r', 'y'], ['p', 'w'], ['l', 'n'], ['o', 'j'], ['t', 'f'], ['q', 'd']] 
	key2=[x[::-1] for x in key] #กำหนด list ชื่อkeyที่มีคู่ลำดับตามที่โจทย์กำหนด
	D=dict(key+key2) #นำ list ทั้งสอง list มาทำคู่อันดับตามที่โจทย์กำหนด
	res='' #กำหนดให้ res มีค่า str ธรรมดา
	for x in message: # ทำการ for loop จาก ตัวแปลที่โจทย์กำหนดให้เพื่อเช็คว่ามีตัวอักษรตามคู่อันดับที่กำหนดหรือไม่ถ้ามีให้ทำการดึงคู่อันดับนั้นมาแล้วนำไป + กับตัวแปล res แต่ถ้าไม่มีให้นำ x+res ทันที ท้ายสุดให้ return res
		if x in D:
			res+=D[x]
		else:
			res+=x
	return res

print(mubashir_cipher("edabit God")) 

print(mubashir_cipher("%$ &%"))

print(mubashir_cipher("not a time"))