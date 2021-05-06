"""
Test.assert_equals(possible_path([1, 'H', 2, 'H', 3, 'H', 4]), True)
Test.assert_equals(possible_path(['H', 3, 'H']), True)
Test.assert_equals(possible_path(['H']), True)
Test.assert_equals(possible_path([3]), True)
Test.assert_equals(possible_path([1, 2, 'H', 3]), False)
Test.assert_equals(possible_path(['H', 1, 3]), False)
Test.assert_equals(possible_path([2, 4, 'H']), False)
Test.assert_equals(possible_path([1, 'H', 1, 'H', 1, 'H']), True)
Test.assert_equals(possible_path([3, 'H', 2, 'H', 3, 'H', 1]), True)
Test.assert_equals(possible_path(['H', 2, 'H', 3, 4, 'H', 1, 'H', 2, 'H']), False)
"""

def possible_path(path):
    k = 0
    for i,d in enumerate(path):
        if i != len(path) - 1:
            if type(d) == type(path[i+1]):
                k += 1
    return True if k == 0 else False

print(possible_path([1, 'H', 2, 'H', 3, 'H', 4]))
print(possible_path(['H', 3, 'H']))
print(possible_path([1, 2, 'H', 3]))
