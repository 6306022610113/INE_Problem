def twins(lst):
    for i in range(len(lst)):
        if sum(lst[:i]) == sum(lst[i:]):
            return i
print(twins([10, 20, 30, 5, 40, 50, 40, 15])) 
print(twins([1, 2, 3, 4, 5, 5])) 
print(twins([3, 3]))            