def capToFront(x):
    cap1,cap2 = '',''
    for i in x:
        if i.isupper():
            cap1 += i
        else:
            cap2 += i
    return cap1 + cap2


print(capToFront('hApPy'))
print(capToFront('moveMENT'))
print(capToFront('shOrtCAKE'))
