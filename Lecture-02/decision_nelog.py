pay = int(input(" ENTER YOUR PAY : "))
bonus = 0
total = 0

if pay > 1000:
    if pay > 2000:
        bonus = 100
    else:
        bonus = 50
else:
    bonus = 10

total = pay + bonus

print("===== SALARY =====")
print("YOUR PAY :",pay)
print("YOUR BONUS :",bonus)
print("YOUR TOTAL :",total)
print("==================")