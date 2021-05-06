def mubashir_cipher(message):
	key= [['m', 'c'], ['u', 'e'], ['b', 'g'], ['a', 'k'], ['s', 'v'], ['h', 'x'],['i', 'z'], ['r', 'y'], ['p', 'w'], ['l', 'n'], ['o', 'j'], ['t', 'f'], ['q', 'd']]
	s=""
	for i in message:
		found=False
		for j in key:
			if i==j[0]:
				found=True
				s+=j[1]
				break
			elif i==j[1]:
				found=True
				s+=j[0]
				break
		if not found:
			s+=i
	return s

print(mubashir_cipher("mubashir is not amazing"))
print(mubashir_cipher("cegkvxzy zv ljf kckizlb"))
print(mubashir_cipher("edabit is amazing !"))
print(mubashir_cipher("%$ &%"), "%$ &%")
print(mubashir_cipher("~!@#$%^&*()_+= -0 98 76 54 3 2 1"))
print(mubashir_cipher("matt && is amazing"))
print(mubashir_cipher("evgeny sh is amazing"))
print(mubashir_cipher("usbulr vx zv kckizlb"))
print(mubashir_cipher("airforce needs me ?"))
print(mubashir_cipher("pakistan is love !"))