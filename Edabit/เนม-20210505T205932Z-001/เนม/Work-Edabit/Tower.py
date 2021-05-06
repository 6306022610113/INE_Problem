def tow(n, f):
    for i in range(1, n):
        f+=1
        f=tow(i,f)
    return f

def tower_hanoi(n):
    return tow(n+1, 0)

print(tower_hanoi(3))

print(tower_hanoi(5))

print(tower_hanoi(0))