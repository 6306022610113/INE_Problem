def sumTwoSmallestNums(str1):
    str1 = sorted(str1)
    lsum = []

    for i in str1:
        if i >= 0 :
            lsum.append(i)
    
    sum = lsum[0] + lsum[1]
    
    return sum

print(sumTwoSmallestNums([19, 5, 42, 2, 77]))
print(sumTwoSmallestNums([10, 343445353, 3453445, 3453545353453]))
print(sumTwoSmallestNums([2, 9, 6, -1]))
print(sumTwoSmallestNums([879, 953, 694, -847, 342, 221, -91, -723, 791, -587]))
print(sumTwoSmallestNums([3683, 2902, 3951, -475, 1617, -2385]))