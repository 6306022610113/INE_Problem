"""
Test.assert_equals(fibonacci(3), 3)
Test.assert_equals(fibonacci(7), 21)
Test.assert_equals(fibonacci(12), 233)
Test.assert_equals(fibonacci(0), 1)
Test.assert_equals(fibonacci(1), 1)
"""

def fibonacci(index):
    fibonacci_number = [1,1]
    for i in range(index):
        fibonacci_number.append(fibonacci_number[i+1]+fibonacci_number[i])
    return fibonacci_number[index]




print(fibonacci(3))
print(fibonacci(7))
print(fibonacci(12))
