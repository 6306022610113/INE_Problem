def return_unique(lst):

    result = []

    for volk in lst:
        if lst.count(volk) < 2:
            result.append(volk)
    return result

print (return_unique([1, 9, 8, 8, 7, 6, 1, 6]))
print (return_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]))
print (return_unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]))