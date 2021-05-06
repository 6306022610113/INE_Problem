def add(n1, n2):
    
    if n1 and n2:
        return str(int(n1)+int(n2))
    else:
        return "Invalid Operation"

print (add("111", "111"))
print (add("10", "80"))
print (add("", "20"))