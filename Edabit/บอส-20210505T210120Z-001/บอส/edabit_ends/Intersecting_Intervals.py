"""
Test.assert_equals(count_overlapping([[1, 2], [2, 3], [3, 4]], 5),0)
Test.assert_equals(count_overlapping([[1, 2], [5, 6], [5, 7]], 5),2)
Test.assert_equals(count_overlapping([[1, 2], [5, 8], [6, 9]], 7),2)
Test.assert_equals(count_overlapping([[1, 5], [2, 5], [3, 6], [4, 5], [5, 6]], 5), 5)
Test.assert_equals(count_overlapping([[1, 5], [2, 5], [3, 6], [4, 5], [5, 6]], 6), 2)
Test.assert_equals(count_overlapping([[1, 5], [2, 5], [3, 6], [4, 5], [5, 6]], 2), 2)
Test.assert_equals(count_overlapping([[1, 5], [2, 5], [3, 6], [4, 5], [5, 6]], 1), 1)
"""

def count_overlapping(data,number):
    total = 0
    for i in data:
        for k in range(i[0],i[-1]+1):
            if k == number:
                total += 1
    return total



print(count_overlapping([[1, 2], [2, 3], [3, 4]], 5))
print(count_overlapping([[1, 2], [5, 6], [5, 7]], 5))
print(count_overlapping([[1, 2], [5, 8], [6, 9]], 7))
