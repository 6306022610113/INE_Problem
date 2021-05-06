def uncensor(txt, vowels):                               ### สร้างฟังก์ชั่นขึ้นมา โดย รับสองค่า คือ คำที่เป็น ตัวอักษรและ * อยู่ใน txt
    sequence_of_vowels = 0                               ### และค่าที่เป็น สระ อยู่ใน vowels สร้างตัวแปล sequence_of_vowels เป็น 0
    answer = ''                                          ### สร้างตัวแปล answer ขึ้นมากำหนด เป็น สตริงปล่าว
    for i in txt:                                        ### สร้าง ลูป for ให้ i เช็ค txt ที่ได้รับมา ว่า
        if i == '*':                                     ### ถ้า i ใน txt ตัวใดเป็น * ให้ใส่ ตัวสระที่รับมาใน vowels ตำแหน่งที่มีค่าของ
            answer += vowels[sequence_of_vowels]         ### sequence_of_vowel ก็คือที่เคยกำหนดไว้ก็คือ 0 ลงไปใน ตัวแปลanswer
            sequence_of_vowels += 1                      ### จากนั้น ให้ sequence_of_vowels += 1 เพื่อครั้งต่อไปให้เอา สระ
        else:                                            ### ตำแหน่งต่อไป แต่ถ้าไม่ใช่ คือถ้า i ใน txt ตัวใดไม่ได้เป็น *
            answer += i                                  ### ให้ ตัวแปล answer += i เข้าไปใน answer
    return answer

print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))
print(uncensor("abcd", ""))
print(uncensor("*PP*RC*S*", "UEAE"))