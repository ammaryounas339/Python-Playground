import threading

def check(a,b):
    if a>= 100 and a<= 200:
        print("in range")

    else : 
        print("a Not in range")
    if b>= 100 and b<= 200:
        print("In range")
    else :
        print("b not in range")

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
t1 = threading.Thread(target=check,args = (a,b))
t1.start()