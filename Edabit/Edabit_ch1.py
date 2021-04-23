def face_interval(num):             #รับค่าตัวแปร num เข้ามา
    if type(num) == list:           #ถ้า num เท่ากับ List
        x = max(num) - min(num)     #ให้นำค่าที่มากที่สุดลบค่าที่น้อยที่สุด
        if x in num:                #ถ้า x มีค่าใน num
            return ":)"             #ให้ส่งค่า :)
        else:
            return ":("             #ถ้าไม่มีให้ส่ง :(
    else:
        return ":/"                 #ถ้าไม่สามารถคำนวณได้ให้ส่ง :/

print(face_interval([1, 2, 5, 8, 3, 9]))
print(face_interval([5, 2, 8, 3, 11]))
print(face_interval("bruh"))