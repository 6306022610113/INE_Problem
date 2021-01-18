def bubble(l):
    def swap(i,j):
        l[i],l[j] = l[j],l[i]

    n = len(l)
    swapped = True

    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if l[i-1] > l[i]:
                swap(i-1 ,i)
                swapped = True
            print(l)


    return l
    
l = [8,3,9,4,5]
bubble(l)