def removeDups(str1):
    reDups = []
    for i in str1:
        if i not in reDups:
            reDups.append(i) 
    return reDups


print(removeDups([1,0,1,0]))
print(removeDups(["The","big","cat"]))
print(removeDups(["John","Taylor","John"]))