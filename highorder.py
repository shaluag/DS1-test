##### LAMBDA FUNCTION
m=lambda a,b,c:a+b+c
print(m(3,4,5))

m=lambda a,b:a+b if a>b else a-b
print(m(3,4))

##### MAP FUNCTION
def square(x):
    return x*x
list1=[3,4,5,6,7]
y=map(square,list1)
[*y]

n=map(lambda x:x*x, list1)
[*n]

list2=[3,4,5,6,7,8]
z=map(lambda x:"even" if x%2==0 else "odd" , list2)
[*z]

####
list3=["hello", "hi", "how"]
q=map(lambda x:len(x), list3)
[*q]

##### REDUCE FUNCTION
from functools import reduce
k=reduce(lambda a,b:a+b, list3)
print(k)

a=reduce(lambda a,b:2 if isinstance(a, str) else a+1, list3)  ### ISINSTANCE FUNCTION
print(a)
list2=[3,4,5,6,7,8]
f=filter(lambda x:True if x%2==0 else False, list2)
[*f]

##### FILTER FUNCTION
# def test(x):
#     if x%2==0:
#         return True
#     else:
#         return False
[*filter(lambda x:True if x%2==0 else False, list2)]

