def largest_even(lst):                             # สร้างฟังก์ชั่นที่ รับค่า ลิสต์มา
    result = -1                                    # สร้างตัวแปล result จากนั้นกำหนดให้เป็น -1
    for i in lst:                                  # สร้างลูปขึ้นมา แล้วมี เงื่อนไขข้างในว่า ถ้า i หาร 2 แล้วได้ 0 และ i มีค่ามากกว่า 
        if i % 2 == 0 and i > result:              # ค่าที่อยู่ใน result ซึ่งก็คือตอนแรกกำหนดให้เป็น -1 ให้ทำการ แทนค่า i
            result = i                             # ลงไปใน result จากนั้นก็วนลูปจนจบ
    return result

print(largest_even([3, 7, 2, 1, 7, 9, 10, 13]))
print(largest_even([1, 3, 5, 7]))
print(largest_even([0, 19, 18973623]))