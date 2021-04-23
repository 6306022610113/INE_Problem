def choose_fuse(fuses, current):        #รับค่า List ของ fases และ current
    new = []                            #สร้างตัวแปรเพื่อมารับค่า
    for f in fuses:                     #ถ้า f มีใน fases
        f = int(f[:-1])                 #แปลงค่า f เป็น int
        if f >= float(current[:-1]):    #ถ้าค่า f มากกว่าเท่ากับ current
            new.append(f)               #ให้เพิ่มเข้าไปในตัวแปร new
    return str(min(new)) + 'V'          #ลงค่าที่น้อยที่สุดของ new ออกไปแบบ str

print(choose_fuse(["3V", "5V", "12V"], "4.5V"))
print(choose_fuse(["5V", "14V", "2V"], "5.5V"))
print(choose_fuse(["17V", "15V", "12V"], "9V"))