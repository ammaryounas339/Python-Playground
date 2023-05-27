from functools import reduce
list1=[2,3,4,9,1,2]
list2 = list(map(lambda x:x*x,list1))
print(list2)

num = reduce(lambda x,y:x if x>y else y,list1)#
print(num)
