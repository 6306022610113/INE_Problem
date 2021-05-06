"""
Test.assert_equals(boom_intensity(0), "boom")
Test.assert_equals(boom_intensity(1), "boom")
Test.assert_equals(boom_intensity(2), "Boom!")
Test.assert_equals(boom_intensity(3), "Booom")
Test.assert_equals(boom_intensity(4), "Boooom!")
Test.assert_equals(boom_intensity(5), "BOOOOOM")
Test.assert_equals(boom_intensity(6), "Boooooom!")
Test.assert_equals(boom_intensity(17), "Booooooooooooooooom")
Test.assert_equals(boom_intensity(18), "Boooooooooooooooooom!")
Test.assert_equals(boom_intensity(19), "Booooooooooooooooooom")
Test.assert_equals(boom_intensity(20), "BOOOOOOOOOOOOOOOOOOOOM!")
Test.assert_equals(boom_intensity(45), "BOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOM")
Test.assert_equals(boom_intensity(46), "Boooooooooooooooooooooooooooooooooooooooooooooom!")
Test.assert_equals(boom_intensity(47), "Booooooooooooooooooooooooooooooooooooooooooooooom")
Test.assert_equals(boom_intensity(100), "BOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOM!")
"""
def boom_intensity(number_o):
    if number_o >= 2:
        text_o = 'o' * number_o
        word = 'B' + text_o + 'm'
        if number_o % 2 == 0:
            word += '!'
        if number_o % 5 == 0:
            word = word.upper()
        return word
    else:
        return 'boom'



print(boom_intensity(4))
print(boom_intensity(1))
print(boom_intensity(5))
print(boom_intensity(10))
