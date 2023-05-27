def prime(num):
    if num<2:
        return False
    for i in range(2,num+1):
        if num % i == 0:
            return False
    return True
lower =  int(input("Enter lower number : "))
higher = int(input("Enter higher number : "))
for i in range(lower,higher+1):
    if prime(i):
        print(i)

