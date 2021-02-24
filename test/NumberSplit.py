def numberSplit(num):
    list_num = []
    num1 = num // 2
    num2 = num // 2 + (num % 2)
    list_num.append(num1)
    list_num.append(num2)
    return list_num

print(numberSplit(4))
print(numberSplit(10))
print(numberSplit(11))
print(numberSplit(-9))