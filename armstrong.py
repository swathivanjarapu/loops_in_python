i=int(input("enter number"))
n=len(str(i))
ret=0
while i!=0:
    digit=i%10
    ret=ret+digit**n
    i=i//10
if i==ret:
    print(ret)
