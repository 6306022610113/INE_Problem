def simple_equation(a, b, c):               #รับค่าตัวเลข a, b, c
    for i in ['+', '-', '*', '//']:         #ถ้า i ใน List
        sum1 = str(a) + i + str(b)          #นำ str(a) สุ่มเครื่องหมาย + - * / กับ str(b)
        if eval(sum1) == c:                 #ถ้าแปลง sum1 ให้เป็น str และต้องเท่ากับ str(c)
            eq = sum1 + "=" + str(c)        #ให้นำ sum1 มาบวกเท่ากับ str(c)
            return eq.replace('//', '/')    #ลงค่า '//' และ '/' สามารถใช้แทนกันได้
    return ""                               #ส่งค่าออก

print(simple_equation(1, 2, 3))
print(simple_equation(2, 2, 4))
print(simple_equation(6, 2, 3))