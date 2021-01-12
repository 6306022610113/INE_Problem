hours = 0
pay_rate = 0
grosspay = 0


def read():
    global hours
    global pay_rate
    hours = int(input("Enter your hours : "))
    pay_rate = int(input("Enter your pay rate : "))

def cal(pay_rate,hours):
    
    return pay_rate*hours

def print1():
    global hours
    global pay_rate
    print(cal(pay_rate,hours))

def main():
    want_more = 'y'
    while want_more.lower() == 'y':
        read()
        print1()
        want_more = input('DO YOU WANT TO CAL AGAIN? (y (yes) or n (no)): ')

main()