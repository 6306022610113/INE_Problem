def dice_game(lst):                                     # สร้างฟังก์ชั่นที่รับ list เข้ามาเป็น เลขที่ ทอยลูกเต๋าทั้งสองชุด จากนั้น
    score = 0                                           # สร้างตัวแปรขึ้นมากำหนดให้เป็น 0
    for a,b in lst:                                     # สร้างลูป ให้ a กับ b เช็คใน list เลขที่ 2 ชุด
        if a == b:                                      # สร้างเงื่อนไขว่า ถ้า a = b ให้ return ค่า 0 ออกมาทันที นั้นหมายถึง
            return 0                                    # ทอยได้ Double นั่นเอง แต่ถ้าเกิดว่า ไม่ได้ ทอยได้ double
        else:                                           # ให้ เลขที่ได้มา + ลงไปใน score จากนั้น return ค่า score
            score += a+b
    return score
print(dice_game([(1, 2), (3, 4), (5, 6)]))
print(dice_game([(1, 1), (5, 6), (6, 4)]))
print(dice_game([(4, 5), (4, 5), (4, 5)]))