def missing_letter(lst):
    for i in range(0, len(lst) - 1):
        if lst[i + 1] != chr(ord(lst[i]) + 1):
            return chr(ord(lst[i]) + 1)


print(missing_letter(["a", "b", "c", "e", "f", "g"]))
print(missing_letter(["O", "Q", "R", "S"]))
print(missing_letter(["t", "u", "v", "w", "x", "z"]))
print(missing_letter(["m", "o"]))

