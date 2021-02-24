import time
def digitalClock(num):
    hours = num // 3600
    minutes = (num % 3600) // 60
    seconds = num % 60


    clock = str.format("{}:{}:{}", hours, minutes, seconds)
    return clock

print(digitalClock(5025))
print(digitalClock(61201))
print(digitalClock(87000))