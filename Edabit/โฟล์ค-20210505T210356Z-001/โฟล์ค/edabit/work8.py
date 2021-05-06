def concat(*args):

    n = []
    for arg in args:
        for item in arg:
            n.append(item)
    return n

print (concat([1, 2, 3], [4, 5], [6, 7]))
print (concat([1], [2], [3], [4], [5], [6], [7]))
print (concat([1, 2], [3, 4]))
print (concat([4, 4, 4, 4, 4]))