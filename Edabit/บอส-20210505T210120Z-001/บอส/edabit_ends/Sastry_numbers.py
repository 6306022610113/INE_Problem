"""
Test.assert_equals(is_sastry(183), True, "Example #1")
Test.assert_equals(is_sastry(184), False, "Example #2")
Test.assert_equals(is_sastry(106755), True, "Example #3")
Test.assert_equals(is_sastry(129987253440921), False)
Test.assert_equals(is_sastry(157175907513603), True)
Test.assert_equals(is_sastry(206611570247935), True)
Test.assert_equals(is_sastry(338752188230098), False)
Test.assert_equals(is_sastry(433610247875715), True)
Test.assert_equals(is_sastry(652333983478884), False)
Test.assert_equals(is_sastry(718717107443715), True)
Test.assert_equals(is_sastry(752199872453889), False)
Test.assert_equals(is_sastry(786704531939448), True)
"""
import math
def is_sastry(number):
    text_number = str(number+1)
    out_number = str(number) + text_number
    test = math.sqrt(int(out_number))
    if test % int(test) == 0:
        return True
    else:
        return False

print(is_sastry(183))
print(is_sastry(184))
print(is_sastry(106755))



