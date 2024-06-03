a=12
s=200
c=20
r=s
s=a
a=r
print("a=",a)
print("s=",s)
print("c=",c)   
if(a>s and a>c):
    print("a is big")
elif(s>a and s>c):
    print("s is big")
else:
    print("c is big")
