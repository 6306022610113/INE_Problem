def number_length(num):

    length = 0
    for i in str(num):
        length += 1
    return length

print (number_length(10))
print (number_length(5000))
print (number_length(0))