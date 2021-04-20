def simple_equation(a, b, c):
    for i in ['+', '-', '*', '//']:
        term = str(a) + i + str(b)
        if eval(term) == c:
            eq = term + "=" + str(c)
            return eq.replace('//', '/')
    return ""

print(simple_equation(1, 2, 3))
print(simple_equation(2, 2, 4))
print(simple_equation(6, 2, 3))