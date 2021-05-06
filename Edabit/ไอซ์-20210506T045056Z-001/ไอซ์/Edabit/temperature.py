def convert(deg):                                                   # สร้างฟังก์ชั่นรับค่า องศาเป็น ที่มี * และ F หรือ C ด้วยมาเป็นสตริง
    if "C" in deg:                                                  # สร้างเงื่อนไขว่า ถ้า มีตัวสตริง C ใน deg ให้ทำการนำตัวที่ 1 ถึง
        return str((round((int(deg[:-2]))*(9/5))+32)) + "*F"        # ตัวที่ -2 คือ ก่อนตัว * จากนั้น เอามาแปลงเป็นตัวเลขโดยใช้ int
    elif "F" in deg:                                                # จากนั้นใช้ 9/5 ก่อนแล้วเอามาคูณกับ เลขที่แปลงเป็น int เมื่อกี้
        return str(round(((int(deg[:-2]))-32) * (5/9))) + "*C"      # คือ เลข องศา จากนั้น นำไป +32 แล้ว +สตริง *F แล้วรีเทิร์น
    else:                                                           # ถ้า ไม่เจอ C ใน deg แต่เจอ F ใน deg ให้ทำเงื่อนไขถัดไปคือ
        return ("error")                                            # นำมาแปลงเป็น int เหมือนเดิมแล้ว -32 ก่อน จากนั้น 5/9 แล้ว
                                                                    # เอา ค่าที่ ได้จากการ -32 มา คูณ กับ ค่าที่ได้จาก 5/9 จากนั้นรีเทิร์น
print(convert("35*C"))                                              # ถ้าไม่เจอทั้ง F และ C ใน deg ให้ทำการ รีเทิร์น error ออกมา
print(convert("19*F"))
print(convert("33"))