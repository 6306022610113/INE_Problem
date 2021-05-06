def square_patch(n):

    result = []

    for i in range(n):
        result.append([n]*n)

    return result

print (square_patch(3))
print (square_patch(5))
print (square_patch(1))
print (square_patch(0))
