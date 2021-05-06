import time

def addUpToV1(n):
    total = 0 
    for i in range(n):
        total += (i+1)

    return(total)

def addUpToV2(n):
    return n * (n+1)/2

n = int(input('Input Value: '))

start = time.time()
print('answer: ', addUpToV1(n))
print('time: ', (time.time()-start)*1000)

start = time.time()
print('answer: ', addUpToV2(n))
print('time: ', (time.time()-start)*1000)
