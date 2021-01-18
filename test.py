
def main():
    number1 = []
    lst1 = ''
    count = 0
    while count != 5 :
        count += 1
        lst1 = input("ENTER YOUR NUMBER : ")
        if not lst1.isalpha():
            number1.append(int(lst1))
    
    for a in range(len(number1)-1, -1,-1):# จาก last ind ถึง ind 0
        swaped = False
        for i in range(a):
            if number1[i] > number1[i+1]:
                tpm = number1[i]
                number1[i] = number1[i+1]
                number1[i+1] = tpm #swap
                print(number1)
                swaped = True
                   
            
        if not swaped:
            break    


main()