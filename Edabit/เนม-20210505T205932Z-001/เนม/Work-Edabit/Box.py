def box(sol):
    if sol == 0:
        return 0
    elif sol %2 == 0:
        return sol
    else:
        return sol+2



print(box(0)) 

print(box(1))

print(box(2)) 