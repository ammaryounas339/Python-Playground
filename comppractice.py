l1=["ssad          ","Snajhvgdgajhdg    ","shkshdjkhdfjkshdjshjsaadad    "]
l2=[x.strip() for x in l1]
print(l2)
l3 = [i for i in range(21) if i%2==0]
print(l3)
l4 =["eVEN" if i%2==0 else "Odd" for i in range(20) ]
print(l4)
l5 = ["FizzBuzz" for i in range(101) if i%3==0 if i%5==0 ]
print(l5)

