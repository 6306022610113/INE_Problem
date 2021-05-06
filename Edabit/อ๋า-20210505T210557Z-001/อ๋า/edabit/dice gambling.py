def rolls(lst):
    total = lst[0]
    for i in range(1,len(lst)):
        if lst[i-1] == 6:
            total += (lst[i] * 2)
        elif lst[i-1] in range(2,6):
            total += lst[i]
    return total

print(rolls([1, 2, 3]))
print(rolls([2, 6, 2, 5])) 
print(rolls([6, 1, 1]))
