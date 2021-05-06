def age_difference(f_age, s_age):           # สร้างฟั่งก์ชั่นรับ อายุ พ่อใน f_age รับอายุลูกไว้ใน s_age
    c = s_age*2                             # สร้างตัวแปล c ขึ้นมา กำหนดว่า ให้เอา s_age คืออายุลูก * 2 จากนั้น เก็บไว้ในตัวแปล c
    if c >= f_age:                          # สร้างเงื่อนไขว่า ถ้าค่าใน c มากกว่าหรือเท่ากับ f_age ให้ ทำการ เอา c - f_age แล้วเก็บใน a
        a = c - f_age                       # แต่ถ้าไม่ตรงเงื่อนไขให้ ทำการเอา f_age - c แล้วเก็บไว้ใน a แทน
    else:                                   # จากนั้น รีเทิร์น a ออกมา
        a = f_age - c
    return a
print(age_difference(36, 7))
print(age_difference(55, 30))
print(age_difference(42, 21))