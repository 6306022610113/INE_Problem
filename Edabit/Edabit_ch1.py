def face_interval(num):
    if type(num) == list:
        x = max(num) - min(num)
        if x in num:
            return ":)"
        else:
            return ":("
    else:
        return ":/"

print(face_interval([1, 2, 5, 8, 3, 9]))
print(face_interval([5, 2, 8, 3, 11]))
print(face_interval("bruh"))