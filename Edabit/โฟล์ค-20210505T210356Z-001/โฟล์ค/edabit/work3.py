def is_harshad(n):

    x = 0
    m = n
    
    while m > 0:
        x = x + m % 10
        m = m // 10
    return not n % x

print (is_harshad(75))
print (is_harshad(171))
print (is_harshad(481)) 
print (is_harshad(89))
print (is_harshad(516)) 
print (is_harshad(200)) 