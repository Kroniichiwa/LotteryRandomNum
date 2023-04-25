from random import randint

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def loopRandom(n):
    i = 0
    while i < n :
        print('คำนวณหวยใบที่' , i+1 ,':',random_with_N_digits(6))
        i+=1

x = int(input('ต้องการคำนวณเลขหวยกี่ใบ : '))

loopRandom(x)



