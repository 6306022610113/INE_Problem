"""
Test.assert_equals(mystery_func(152), 10)
Test.assert_equals(mystery_func(832), 48)
Test.assert_equals(mystery_func(5511), 25)
Test.assert_equals(mystery_func(19), 9)
Test.assert_equals(mystery_func(133), 9)
"""

def mystery_func(number):
    text_number = str(number)
    n = 1
    for k in text_number:
        p = n * int(k)
        n=p
    return n


print(mystery_func(152))
print(mystery_func(832))
print(mystery_func(19))
print(mystery_func(133))