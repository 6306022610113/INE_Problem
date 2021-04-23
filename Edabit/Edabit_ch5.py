def choose_fuse(fuses, current):
    new = []
    for f in fuses:
        f = int(f[:-1])
        if f >= float(current[:-1]):
            new.append(f)
    return str(min(new)) + 'V'

print(choose_fuse(["3V", "5V", "12V"], "4.5V"))
print(choose_fuse(["5V", "14V", "2V"], "5.5V"))
print(choose_fuse(["17V", "15V", "12V"], "9V"))