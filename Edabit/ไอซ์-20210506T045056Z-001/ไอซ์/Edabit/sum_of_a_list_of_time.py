def time_sum(times):                                        # สร้างฟังก์ชั่นที่รับค่าเวลามา โดยโจทย์ให้มาเป็น ลิสต์ จากนั้น
    hrs, mins, secs = 0, 0, 0                               # สร้างตัวแปล hrs, mins, secs ตั้งให้เป็น 0 ทั้ง 3 ตัว
    for i in times:                                         # สร้างลูปขึ้นมาให้ i เช็คที่ละก้อนที่มีใน list ก่อน โดยเมื่อ list ก้อนแรก
        hours , minutes, seconds = map(int, i.split(':'))   # ได้เช็คจากนั้น ใช้คำสั่ง split โดย : ออกให้เป็น ก้อนเก็บไว้ใน
        hrs += hours                                        # hours , minutes , seconds ต่อมาให้ เอาค่าตัวแปลใน hours ที่ได้มา +
        mins += minutes                                     # ลงในตัวแปล hrs จากนั้น , เอาค่าในตัวแปล minutes ที่ได้มา + ลงใน
        secs += seconds                                     # ตัวแปล mins และ เอาค่าใน seconds ที่ได้มา + ลงในตัวแปล secs
    mins += secs // 60                                      # จากนั้นเอาค่าใน secs มา // 60 คือการหารไม่เอาเศษ จากนั้น + ลงไปใน
    secs = secs % 60                                        # mins จากนั้นกำหนดค่า secs ให้เท่ากับ secs ที่ % การหารเอาแต่เศษ 
    hrs += mins // 60                                       # ขั้นต่อมาให้ นำค่าใน mins มา // 60 คือหารไม่เอาเศษ จากนั้น + ลงใน
    mins = mins % 60                                        # hrs จากนั้นกำหนดให้ mins = mins ที่ % 60
    return [hrs, mins, secs]                                # จากนั้น return hrs, mins, secs ออกมา

print(time_sum(["1:23:45"]))
print(time_sum(["1:03:45", "1:23:05"]))
print(time_sum(["5:39:42", "10:02:08", "8:26:33"]))